from dataclasses import dataclass
from enum import Enum
from typing import List
from datetime import datetime
from decimal import Decimal

class OrderStatus(Enum):
    RECEIVED = 'Recebido'
    PREPARING = 'Em preparação'
    READY = 'Pronto'
    FINALIZED = 'Finalizado'

@dataclass
class Customer:
    id: int = None
    cpf: str = None
    name: str = None
    email: str = None

@dataclass
class Category:
    id: int = None
    name: str = None

@dataclass
class Product:
    id: int = None
    name: str = None
    description: str = None
    price: Decimal = None
    category: Category = None
    image_url: str = None

@dataclass
class OrderItem:
    product: Product
    quantity: int

@dataclass
class Order:
    id: int = None
    customer: Customer = None
    items: List[OrderItem] = None
    status: OrderStatus = OrderStatus.RECEIVED
    payment_status: str = 'Pendente'
    created_at: datetime = None