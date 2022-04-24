from discord.ext.commands import command
import discord
import resurgence
import Spell_book as sb


@command()
async def sheet_create(ctx,file,userid_ctx,username):
  await ctx.send("New character detected! Extracting Data...", delete_after=30)
  character_name=file["name"]
  resurgence.gc.copy("1L9imnQ2RDg55lTQ_pxm2eMJ8TiFRk6Xr-am3SFVfKM8", title=f"{character_name}_Gsheet_v2.1_SW5e", copy_permissions=True)
  work = resurgence.gc.open(f"{character_name}_Gsheet_v2.1_SW5e")
  work.share(value=None,perm_type="anyone", role="reader", with_link=True)
  image=file["image"]
  player=file["user"]
  exp=file["experiencePoints"]
  species=file["species"]["name"]
  classes = file["classes"]
  base_str=file["baseAbilityScores"]["Strength"]
  base_dex=file["baseAbilityScores"]["Dexterity"]
  base_con=file["baseAbilityScores"]["Constitution"]
  base_int=file["baseAbilityScores"]["Intelligence"]
  base_wis=file["baseAbilityScores"]["Wisdom"]
  base_cha=file["baseAbilityScores"]["Charisma"]
  align=file["characteristics"]["alignment"]
  personality=file["characteristics"]["Personality Traits"]
  ideal=file["characteristics"]["Ideal"]
  bond=file["characteristics"]["Bond"]
  flaw=file["characteristics"]["Flaw"]
  gender=file["characteristics"]["Gender"]
  age=file["characteristics"]["Age"]
  height=file["characteristics"]["Height"]
  weight=file["characteristics"]["Weight"]
  hair=file["characteristics"]["Hair"]
  eyes=file["characteristics"]["Eyes"]
  skin=file["characteristics"]["Skin"]
  appearance=file["characteristics"]["Appearance"]
  backstory=file["characteristics"]["Backstory"]
  background=file["background"]["name"]
  feature=file["background"]["feature"]
  feat=[]
  feat.append(file["background"]["feat"]["name"])
  
  _class=[]
  _forcePowers=[]
  _levels=[]
  _techPowers=[]
  _archetype=[]
  _bonus_abscore={'Strength':0,'Dexterity':0,'Constitution':0,'Intelligence':0,'Wisdom':0,'Charisma':0}

  for key in file["species"]["abilityScoreImprovement"]:
    _bonus_abscore.update({key:_bonus_abscore[key]+file["species"]["abilityScoreImprovement"][key]})
  for items in classes:
    _class.append(items["name"])
    _levels.append(items["levels"])
    for i in items["abilityScoreImprovements"]:
      if i["type"]=="Ability Score Improvement":
        for j in i["abilitiesIncreased"]:
          _bonus_abscore.update({j["name"]:_bonus_abscore[j["name"]]+j["value"]})
      else:
        feat.append(i["name"])
    if "forcePowers" in items:
      _forcePowers.extend(items["forcePowers"])
    else:
      pass
    if "techPowers" in items:
      _techPowers.extend(items["techPowers"])
    else:
      pass
    if "archetype" in items:
      _archetype.append(items["archetype"])

    _forcePowers.extend(file["customForcePowers"])
    _techPowers.extend(file["customTechPowers"])

  level=""
  class_level= dict(zip(_class, _levels))
  
  if(len(_forcePowers)):
    if "Light" in align:
      if "Sentinel" in _class:
        level=level+"SentinelLight"+" "+str(class_level["Sentinel"])+" "
        spell_class="Sentinellight"
        del class_level["Sentinel"]
      if "Guardian" in _class:
        level=level+"GuardianLight"+" "+str(class_level["Guardian"])+" "
        spell_class="Guardianlight"
        del class_level["Guardian"]
      if "Consular" in _class:
        level=level+"ConsularLight"+" "+str(class_level["Consular"])+" "
        spell_class="Consularlight"
        del class_level["Consular"]
    elif "Dark" in align:
      if "Sentinel" in _class:
        level=level+"SentinelDark"+" "+str(class_level["Sentinel"])+" "
        spell_class="Sentineldark"
        del class_level["Sentinel"]
      if "Guardian" in _class:
        level=level+"GuardianDark"+" "+str(class_level["Guardian"])+" "
        spell_class="Guardiandark"
        del class_level["Guardian"]
      if "Consular" in _class:
        level=level+"ConsularDark"+" "+str(class_level["Consular"])+" "
        spell_class="Consulardark"
        del class_level["Consular"]
    else:
      pass
    for key in class_level:
      level=level+str(key)+" "+str(class_level[key])+" "
  else:
    spell_class=""
    for key in class_level:
      level=level+str(key)+" "+str(class_level[key])+" "

  spell0=[]
  spell1=[]
  spell2=[]
  spell3=[]
  spell4=[]
  spell5=[]
  spell6=[]
  spell7=[]
  spell8=[]
  spell9=[]

  check=0
  for item in _forcePowers:
    if item in sb.Force_book:
      vars()[f"spell{sb.Force_book[item]}"].append(item)
      
  for item in _techPowers:
    if item in sb.Tech_book:
      vars()[f"spell{sb.Tech_book[item]}"].append(item)



    
  if len(spell0)>9 or len(spell1)>15 or len(spell2)>15:
    check=1


  await ctx.send("""Data Extracted! Writing to Google Sheets, please be paient.\n**Note: Skill proficiences, Equipment and attacks must be entered manually**""", delete_after=30)
      
  try:
    work.sheet1.batch_update([{'range': 'C16:D16','values': [[base_str,_bonus_abscore['Strength']]]},
                            {'range': 'C21:D21','values': [[base_dex,_bonus_abscore['Dexterity']]]},
                            {'range': 'C26:D26','values': [[base_con,_bonus_abscore['Constitution']]]},
                            {'range': 'C31:D31','values': [[base_int,_bonus_abscore['Intelligence']]]},
                            {'range': 'C36:D36','values': [[base_wis,_bonus_abscore['Wisdom']]]},
                            {'range': 'C41:D41','values': [[base_cha,_bonus_abscore['Charisma']]]},
                            {'range': 'T7:AD7','values': [[species]]},
                            {'range': 'AE7:AG7','values': [[exp]]},
                            {'range': 'C6:R7','values': [[character_name]]},
                            {'range': 'T5:AJ5','values': [[sum(_levels),username]]},
                            {'range': 'AE12:AN14','values': [[personality]]},
                            {'range': 'AE16:AN18','values': [[ideal]]},
                            {'range': 'AE20:AN22','values': [[bond]]},
                            {'range': 'AE24:AN26','values': [[flaw]]},
                            {'range': 'C148:N148','values': [[age,height,weight]]},
                            {'range': 'C150:N150','values': [[gender,eyes,hair,skin]]},
                            {'range': 'AJ11:AN11','values': [[background]]},
                            {'range': 'AJ28:AN28','values': [[align]]},
                            {'range': 'C176:H176','values': [[image]]},
                            {'range': 'T5:AD5','values':[[level]]},
                            {'range': 'C91:R92','values':[[spell_class]]},
                            {'range': 'R165:AN177','values': [[backstory]]}])
  except:
    await ctx.channel.send("Malformed data. Check the file for errors. Exiting...")

  return work.url
#,appearance


@command()
async def sheet_update(ctx,file,userid_ctx,sheet_url,username):
  await ctx.channel.send("Existing character detected! Updating Data...", delete_after=30)
  character_name=file["name"]
  work = resurgence.gc.open_by_url(sheet_url)
  work.share(value=None,perm_type="anyone", role="reader", with_link=True)
  image=file["image"]
  exp=file["experiencePoints"]
  species=file["species"]["name"]
  classes = file["classes"]
  base_str=file["baseAbilityScores"]["Strength"]
  base_dex=file["baseAbilityScores"]["Dexterity"]
  base_con=file["baseAbilityScores"]["Constitution"]
  base_int=file["baseAbilityScores"]["Intelligence"]
  base_wis=file["baseAbilityScores"]["Wisdom"]
  base_cha=file["baseAbilityScores"]["Charisma"]
  align=file["characteristics"]["alignment"]
  personality=file["characteristics"]["Personality Traits"]
  ideal=file["characteristics"]["Ideal"]
  bond=file["characteristics"]["Bond"]
  flaw=file["characteristics"]["Flaw"]
  gender=file["characteristics"]["Gender"]
  age=file["characteristics"]["Age"]
  height=file["characteristics"]["Height"]
  weight=file["characteristics"]["Weight"]
  hair=file["characteristics"]["Hair"]
  eyes=file["characteristics"]["Eyes"]
  skin=file["characteristics"]["Skin"]
  appearance=file["characteristics"]["Appearance"]
  backstory=file["characteristics"]["Backstory"]
  background=file["background"]["name"]
  feature=file["background"]["feature"]
  feat=[]
  feat.append(file["background"]["feat"]["name"])
  
  _class=[]
  _forcePowers=[]
  _levels=[]
  _techPowers=[]
  _archetype=[]
  _bonus_abscore={'Strength':0,'Dexterity':0,'Constitution':0,'Intelligence':0,'Wisdom':0,'Charisma':0}

  for key in file["species"]["abilityScoreImprovement"]:
    _bonus_abscore.update({key:_bonus_abscore[key]+file["species"]["abilityScoreImprovement"][key]})
  for items in classes:
    _class.append(items["name"])
    _levels.append(items["levels"])
    for i in items["abilityScoreImprovements"]:
      if i["type"]=="Ability Score Improvement":
        for j in i["abilitiesIncreased"]:
          _bonus_abscore.update({j["name"]:_bonus_abscore[j["name"]]+j["value"]})
      else:
        feat.append(i["name"])
    if "forcePowers" in items:
      _forcePowers.extend(items["forcePowers"])
    else:
      pass
    if "techPowers" in items:
      _techPowers.extend(items["techPowers"])
    else:
      pass
    if "archetype" in items:
      _archetype.append(items["archetype"])

    _forcePowers.extend(file["customForcePowers"])
    _techPowers.extend(file["customTechPowers"])

  level=""
  
  class_level= dict(zip(_class, _levels))
  
  if(len(_forcePowers)):
    if "Light" in align:
      if "Sentinel" in _class:
        level=level+"SentinelLight"+" "+str(class_level["Sentinel"])+" "
        spell_class="Sentinellight"
        del class_level["Sentinel"]
      if "Guardian" in _class:
        level=level+"GuardianLight"+" "+str(class_level["Guardian"])+" "
        spell_class="Guardianlight"
        del class_level["Guardian"]
      if "Consular" in _class:
        level=level+"ConsularLight"+" "+str(class_level["Consular"])+" "
        spell_class="Consularlight"
        del class_level["Consular"]
    elif "Dark" in align:
      if "Sentinel" in _class:
        level=level+"SentinelDark"+" "+str(class_level["Sentinel"])+" "
        spell_class="Sentineldark"
        del class_level["Sentinel"]
      if "Guardian" in _class:
        level=level+"GuardianDark"+" "+str(class_level["Guardian"])+" "
        spell_class="Guardiandark"
        del class_level["Guardian"]
      if "Consular" in _class:
        level=level+"ConsularDark"+" "+str(class_level["Consular"])+" "
        spell_class="Consulardark"
        del class_level["Consular"]
    else:
      pass
    for key in class_level:
      level=level+str(key)+" "+str(class_level[key])+" "
  else:
    spell_class=""
    for key in class_level:
      level=level+str(key)+" "+str(class_level[key])+" "

      
  spell0=[]
  spell1=[]
  spell2=[]
  spell3=[]
  spell4=[]
  spell5=[]
  spell6=[]
  spell7=[]
  spell8=[]
  spell9=[]
 
  check=0
  for item in _forcePowers:
    if item in sb.Force_book:
      vars()[f"spell{sb.Force_book[item]}"].append(item)
      
  for item in _techPowers:
    if item in sb.Tech_book:
      vars()[f"spell{sb.Tech_book[item]}"].append(item)

  
  if len(spell0)>9 or len(spell1)>15 or len(spell2)>15:
    check =1

  

  await ctx.send("""Data Extracted! Writing to Google Sheets, please be paient.\n**Note: Skill proficiences, Equipment and attacks must be entered manually**""", delete_after=30)
  
  try:
    work.sheet1.batch_update([{'range': 'C16:D16','values': [[base_str,_bonus_abscore['Strength']]]},
                            {'range': 'C21:D21','values': [[base_dex,_bonus_abscore['Dexterity']]]},
                            {'range': 'C26:D26','values': [[base_con,_bonus_abscore['Constitution']]]},
                            {'range': 'C31:D31','values': [[base_int,_bonus_abscore['Intelligence']]]},
                            {'range': 'C36:D36','values': [[base_wis,_bonus_abscore['Wisdom']]]},
                            {'range': 'C41:D41','values': [[base_cha,_bonus_abscore['Charisma']]]},
                            {'range': 'T7:AD7','values': [[species]]},
                            {'range': 'AE7:AG7','values': [[exp]]},
                            {'range': 'C6:R7','values': [[character_name]]},
                            {'range': 'T5:AJ5','values': [[sum(_levels),username]]},
                            {'range': 'AE12:AN14','values': [[personality]]},
                            {'range': 'AE16:AN18','values': [[ideal]]},
                            {'range': 'AE20:AN22','values': [[bond]]},
                            {'range': 'AE24:AN26','values': [[flaw]]},
                            {'range': 'C148:N148','values': [[age,height,weight]]},
                            {'range': 'C150:N150','values': [[gender,eyes,hair,skin]]},
                            {'range': 'AJ11:AN11','values': [[background]]},
                            {'range': 'AJ28:AN28','values': [[align]]},
                            {'range': 'C176:H176','values': [[image]]},
                            {'range': 'T5:AD5','values':[[level]]},
                            {'range': 'C91:R92','values':[[spell_class]]},
                            {'range': 'R165:AN177','values': [[backstory]]}])
    
  except:
    await ctx.channel.send("Malformed data. Check the file for errors. Exiting...")
    return 

  return
 #{'range': 'C59:AN85','values': [[feat,_archetype,feature,appearance]]},