from typing import Union, List, Dict
import json
import os
import yaml
import uvicorn
from pydantic import BaseModel
from fastapi import HTTPException
from fastapi import FastAPI, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import Response
from typing import Optional





app = FastAPI()

#Initializing the app with FastAPI


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Default to port 8000 if PORT is not set
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins="https://ikomovone-cv.onrender.com",
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers="*",

)




class InfoUpdate(BaseModel):
    message: str
    
class CardUpdate(BaseModel):
    serviceName: str
    serviceDescription: str
    serviceLink: str

# Load the configuration from the YAML file

class NewOrder(BaseModel):
    userCardOrder: List[str]
    newOrder: List[str]
    isDefault: bool

#Cross-origin Resource Sharing middleware settings.


class InfoUpdate(BaseModel):
    message: str

#Simple class for updating InfoArea value

class ShowUserNameUpdate(BaseModel):
    showUserName: bool

class customisedAppNameUpdate(BaseModel):
    customisedAppName: str


current_dir = os.path.dirname(__file__)
conf_path = os.path.join(current_dir, 'server_conf.yaml')
json_info_file_path = os.path.join(current_dir, 'assets', 'info.json')

ERROR_CONNECTION_NOT_SAFE = 400
ERROR_USER_NOT_AUTHORIZED = 401

#File addresses, initialization commands




#--------Methods start here-------

def load_config(conf_path):
    with open(conf_path, 'r') as file:
        config = yaml.safe_load(file)
        settings = config["backend"]

        return settings
    


    



    
def load_info_json(json_info_file_path): 
    with open(json_info_file_path, 'r') as info_file:

      info_data= json.load(info_file)
      
      info_item= info_data[0]
      
      return info_item
    



current_dir = os.path.dirname(__file__)
conf_path = os.path.join(current_dir, 'server_conf.yaml')





json_info_file_path = os.path.join(current_dir, 'assets', 'info.json')



# Get all the applications based on the user role
def get_applications(headers: Dict[str, str]) -> List[Dict[str, str]]:

    # Load configuration from configuration file

    
    info_item = load_info_json(json_info_file_path)
    #Load cards information and info area message data

    # Get the user's role from the headers
    user_is_admin = "True"
    
    # List to store applications
    applications = []
    
    # Get a message from the info_item, defaulting to "No message found" if not present
    message = info_item.get("message", "No message found")
    
    
    # Attach message and user role to the response
    version = info_item.get("Version", "No version found")


    applications.append({"message": message, "user_role": user_is_admin, "version": version})
    


   

   
    
    
   
    return applications






def handle_error(error_message, error_code):
    return [{"error": error_message, "code": str(error_code)}]




























#--------APIs start here-------




#API for updating the infoArea. Updates the text in the configuration file.

@app.post("/info/")
async def update_info(request: Request, info_update: InfoUpdate):

    post_headers = dict(request.headers)
    
    security_token = post_headers.get("x-security-token")


    conf = load_config(conf_path)
    api_key = conf["api_key"]  

    ##api_key= "11"                           #wrong api_key for testing purposes

    api_token = post_headers.get("x-api-token")

    


    if int(api_key) != int(api_token):
       return handle_error("Connection is not safe.", ERROR_CONNECTION_NOT_SAFE)
    elif security_token== None:
       return handle_error("User not authorized", ERROR_USER_NOT_AUTHORIZED)
    
    else:

        # Load info data from JSON file
        current_dir = os.path.dirname(__file__)
        json_info_file_path = os.path.join(current_dir, 'assets', 'info.json')

        with open(json_info_file_path, 'r') as info_file:
            info_data = json.load(info_file)
            # Update the message
            info_data[0]["message"] = info_update.message
        # Write updated data back to JSON file
        with open(json_info_file_path, 'w') as info_file:
            json.dump(info_data, info_file, indent=4)
        return [{
          
          "response": "200"
       }]
       
    















    
    
    
    
    
    





    
    



#API for returning applications information based on the user type.
@app.get("/applications/", response_model=List[Dict[str, str]])
async def applications(request: Request):

    headers = dict(request.headers)
    #security_token = headers.get("x-security-token")

    conf = load_config(conf_path)
    api_key = conf["api_key"]         
    


   

    #user_role = headers.get("x-user-roles")
    #api_token = headers.get("x-api-token")


    applications = get_applications(headers)

    #Checking if authentication security token is present, respond with rejection if no token.

    #if int(api_key) != int(api_token):
       #return handle_error("Connection is not safe.", ERROR_CONNECTION_NOT_SAFE)
    #elif security_token== None:
       #return handle_error("User not authorized", ERROR_USER_NOT_AUTHORIZED)
    
    #else:
       
       #Return applications info if token is present.

    



    return applications
    

























#API for returning the user type. 
@app.get("/identify/")
async def identify_user(request: Request):
    
    user_headers = dict(request.headers)


    

    conf = load_config(conf_path)
    
    api_key = conf["api_key"]         

    #api_token = user_headers.get("x-api-token")
    
    return user_headers.get("x-user-roles")



# API for returning UI language


@app.get("/language/{lan_code}")
async def get_language(lan_code: str):
    current_dir = os.path.dirname(__file__)
    json_language_file_path = os.path.join(current_dir, 'assets', 'language.json')
    
    with open(json_language_file_path, 'r') as language_file:
        language_data = json.load(language_file)

    for language in language_data:
        if language['lanCode'] == lan_code:
            return language

    raise HTTPException(status_code=404, detail="Language not found")