from sqlalchemy.orm import Session
from fastapi import Body, FastAPI, Response , status , HTTPException , Depends , APIRouter
from .. import models, schemas, oauth2
from ..database import get_db
from typing import Optional, List

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return {"data": posts}

# request Get method url
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),current_user: int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0,search: Optional[str] = ""):
    posts = db.query(models.Post).filter(
        models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    results = db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()

    print(results)
    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db), user_id:int = Depends(oauth2.get_current_user),
limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    #cursor.execute("""INSERT INTO posts (title,content,published,id) VALUES (%s,%s,%s,%s) RETURNING """,(post.title, post.content, post.published,post.id))
    #new_post = cursor.fetchone()
    #conn.commit()
    print(user_id)
    new_post = models.Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

@router.get("/{id}")
def get_post(id: int,db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    print(post)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f"post with id: {id} was not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'message':f"post with id : {id} was not found"}
    return {"post_detail": post}

@router.get("/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail": post} 

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db)):
    #cursor.execute("""DELETE FROM posts WHERE id = %s returning *""",(str(id),))
    #deleted_post = cursor.fetchone()
    #conn.commit()
    post = db.query(models.Post).filter(models.Post.id == id)

    
    if post.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
 
    post.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate ,db: Session = Depends(get_db)):

    #cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""",(post.title,post.content,post.published,str(id)))
    post_query = db.query(models.Post).filter(models.Post.id == id)
    
    #post = post_query.first()
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"post with id: {id} does not exist")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    
    db.commit()

    return {"data": post_query.first()}


@router.post("/", status_code=status.HTTP_201_CREATED,response_model= schemas.Post)
def create_posts(post:schemas.PostCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

     new_post = models.Post(owner_id=current_user.id,**post.dict())
     db.add(new_post)
     db.commit()



@router.put("/{id", response_model = schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate,db: Session = Depends(get_db),
current_user: int = Depends(oauth2.get_current_user)):

   

   posts_query = db.query(models.Post).filter(models.Post.id == id)

   post = posts_query.first()

   if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id: {id} does not exist")

   if post.owner.id != oauth2.get_current_user.id:
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN,
                           detail="Not authorized to perform requested")

   posts_query.update(updated_post.dict(), synchronize_session=False)

   db.commit()

