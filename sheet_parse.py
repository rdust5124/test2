import ctx as ctx
import sqlite3
from lib.db import db
import template_sheet_create
from discord.ext.commands import command

db.build()


@command(hidden=True)
async def sheet_exist(ctx,userid_ctx, file,username):
  file_id = file['id']
  file_id = file_id.replace("-", "")
  conn = sqlite3.connect('./data/db/database.db',check_same_thread=False)
  cursor_obj = conn.cursor()
  cursor_obj.execute("SELECT * FROM FILEIDTABLE where FILEID=(?)",(file_id,))
  data = cursor_obj.fetchall()
  if len(data)==0:
    sheet_url = await template_sheet_create.sheet_create(ctx,file,userid_ctx,username)
    cursor_obj.execute("INSERT INTO FILEIDTABLE VALUES (?,?,?)",(file_id,userid_ctx,sheet_url))
    conn.commit()
    print("a")
    return sheet_url
  else:
    await template_sheet_create.sheet_update(ctx,file,userid_ctx,data[0][2],username)
    print("b")
    return data[0][2]

