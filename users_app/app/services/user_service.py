from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas import UserCreate, UserLogin, UserUpdate
from app.utils import hash_password, verify_password
from app.auth import create_access_token
import uuid
from datetime import datetime, timedelta

# Clase UserService
class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    # Crear un usuario
    def create_user(self, user: UserCreate):
        # 1. Validar unicidad
        if self.repository.get_by_username(user.username):
            raise HTTPException(status_code=412, detail="El usuario ya existe")
        
        if self.repository.get_by_email(user.email):
            raise HTTPException(status_code=412, detail="El email ya existe")
        
        # 2. Hash password
        hashed_pwd, salt = hash_password(user.password)
        
        # 3. Preparar datos
        user_data = {
            "id": str(uuid.uuid4()),
            "username": user.username,
            "email": user.email,
            "password": hashed_pwd,
            "salt": salt,
            "fullName": user.fullName,
            "phoneNumber": user.phoneNumber,
            "dni": user.dni,
            "createdAt": datetime.utcnow(),
            "updatedAt": datetime.utcnow(),
            "status": "POR_VERIFICAR"
        }
        
        return self.repository.create(user_data)

    # Login
    def login_user(self, credentials: UserLogin):
        user = self.repository.get_by_username(credentials.username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
            
        if not verify_password(credentials.password, user.password, user.salt):
            raise HTTPException(status_code=404, detail="Incorrect password")
            
        token = create_access_token()
        expire_at = datetime.utcnow() + timedelta(hours=24)
        
        return self.repository.save_token(user, token, expire_at)
    
    def update_user(self, id: str, user_update: UserUpdate):
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
            
        update_data = user_update.model_dump(exclude_unset=True)
        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")
            
        if "status" in update_data:
             if update_data["status"] not in ["POR_VERIFICAR", "NO_VERIFICADO", "VERIFICADO"]:
                 raise HTTPException(status_code=400, detail="Invalid status")
                 
        return self.repository.update(user, update_data)
    

    def get_user_by_id(self, id: str):
        user = self.repository.get_by_id(id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    # Contar usuarios
    def get_count(self):
        return self.repository.count()
    
    # Resetear la ddbb
    def reset_db(self):
        self.repository.delete_all()
