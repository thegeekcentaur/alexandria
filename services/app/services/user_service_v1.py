__author__ = 'archanda'
__date__ = '3-Oct-2021'
__copyright__ = "Copyright 2021"
__credits__ = ["archanda"]
__license__ = "All rights reserved"
__maintainer__ = "archanda"
__email__ = "2020mt93064@wilp.bits-pilani.ac.in"
__status__ = "dev"

from fastapi import FastAPI, Body, APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# route-specific modules go here
from api.routes import urls

router = APIRouter()

# Render welcome message
@router.get('/', response_class=HTMLResponse)
async def user_management(response: Response, request: Request):
    return "Welcome to user management, coming soon"
