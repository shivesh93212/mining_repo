from fastapi import APIRouter
from app.schemas.schemas import OptimizationRequest
from app.services.optimization_service import optimize_parameters

router = APIRouter()

@router.post("/")
def optimize_operation(request: OptimizationRequest):
    result = optimize_parameters(request.current_speed, request.current_load, request.target_efficiency)
    return {"optimized_parameters": result, "message": "Optimization complete"}