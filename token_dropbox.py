import dropbox
import os

dbx = dropbox.Dropbox(
    oauth2_refresh_token="VakTOkpcTIQAAAAAAAAAARbfDg9PF4sSYrjuTuIS9_FtkTZUMtP_z4Pbt9XafPAO",
    app_key="hmvqrha0wy3iboj",
    app_secret="iyf6mrishspxokb"
)


local_files = {
    "Client_access_token.csv": r"C:/QUANT_TEAM\DATABASE/XTS_Access_Token/Access_token_interactive_api_xts/Client_access_token.csv",
    "Marketdata_access_token.csv": r"C:/QUANT_TEAM\DATABASE/XTS_Access_Token/Access_token_marketdata_api_xts/Marketdata_access_token.csv",
    "access_token.csv": r"C:/QUANT_TEAM/Telegram_bot/pyscript/access_token.csv"
}

dropbox_folder = "/xts_access_token"

for filename, local_path in local_files.items():
    dropbox_path = f"{dropbox_folder}/{filename}"  
    
    if os.path.exists(local_path):
        with open(local_path, "rb") as f:
            dbx.files_upload(
                f.read(),
                dropbox_path,
                mode=dropbox.files.WriteMode("overwrite")  
            )
        print(f"Uploaded {local_path} → {dropbox_path}")
    else:
        print(f"File not found: {local_path}")