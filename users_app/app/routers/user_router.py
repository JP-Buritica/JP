from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserCreate, UserResponse, UserLogin, Token, UserUpdate
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.models import User
from app.auth import get_current_user

# Creación del router
router = APIRouter(prefix="/users", tags=["users"])

# Dependencias
def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repository = UserRepository(db)
    return UserService(repository)

# --- Endpoints ---

# Health check
@router.get("/ping")
def health_check():
    return "pong"

# Resetear la ddbb
@router.post("/reset")
def reset_db(service: UserService = Depends(get_user_service)):
    service.reset_db()
    return {"msg": "Todos los datos fueron eliminados"}

# Crear un usuario
@router.post("", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, service: UserService = Depends(get_user_service)):
    new_user = service.create_user(user)
    return {
        "id": new_user.id,
        "createdAt": new_user.createdAt.isoformat()
    }

# Login
@router.post("/auth", response_model=Token)
def login(credentials: UserLogin, service: UserService = Depends(get_user_service)):
    user = service.login_user(credentials)
    return {
        "id": user.id,
        "token": user.token,
        "expireAt": user.expireAt
    }

# Obtener el usuario actual
@router.get("/me", response_model=UserResponse)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# Actualizar un usuario
@router.patch("/{id}")
def update_user(id: str, user_update: UserUpdate, service: UserService = Depends(get_user_service)):
    service.update_user(id, user_update)
    return {"msg": "el usuario ha sido actualizado"}

# Contar usuarios
@router.get("/count")
def count_users(service: UserService = Depends(get_user_service)):
    count = service.get_count()
    return {"count": count}
