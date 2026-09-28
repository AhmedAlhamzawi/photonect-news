"""Pexels + Commons contact sheet for image hunting. Red label = already used in a past _image_credits_*.json.
Usage: OUT=/some/dir python3 scripts/image_contact_sheet.py <name> "px:query" "cm:commons query" ...
Writes $OUT/sheet_<name>.jpg + sheet_<name>.json (index -> pexels id / Commons File: title)."""
import json,sys,io,urllib.request,urllib.parse,glob,os
OUT=os.environ.get('OUT','/tmp')
from PIL import Image,ImageDraw,ImageFont
from concurrent.futures import ThreadPoolExecutor
ROOT="/Users/ahmed/Desktop/Photonect NEWS/NEWS CODE"
UA={"User-Agent":"PhotonectNewsBot/1.0 (https://photonect.net; ahmed@photonect.net)"}
key=[l.split("=",1)[1].strip().strip('"') for f in (".env.local",".env") if os.path.exists(f"{ROOT}/{f}") for l in open(f"{ROOT}/{f}") if l.startswith("PEXELS_API_KEY=")][0]
used=set()
for f in glob.glob(f"{ROOT}/scripts/_image_credits_*.json"):
    for v in json.load(open(f)).values():
        used.add(v.get("page","") if isinstance(v,dict) else str(v))
def get(u,h=UA): return urllib.request.urlopen(urllib.request.Request(u,headers=h),timeout=60).read()
def pexels(q,n=12):
    d=json.loads(get("https://api.pexels.com/v1/search?"+urllib.parse.urlencode({"query":q,"per_page":n,"orientation":"portrait"}),{**UA,"Authorization":key}))
    return [(f"px{p['id']}",p["src"]["medium"],p["url"] in used) for p in d["photos"]]
def commons(q,n=12):
    d=json.loads(get("https://commons.wikimedia.org/w/api.php?"+urllib.parse.urlencode({"action":"query","format":"json","generator":"search","gsrsearch":q+" filetype:bitmap","gsrnamespace":6,"gsrlimit":n,"prop":"imageinfo","iiprop":"url","iiurlwidth":300})))
    return [(p["title"],p["imageinfo"][0]["thumburl"],False) for p in d.get("query",{}).get("pages",{}).values()]
name=sys.argv[1]; items=[]
for q in sys.argv[2:]:
    src,qq=q.split(":",1)
    try: items+= (pexels if src=="px" else commons)(qq)
    except Exception as e: print("ERR",q,e)
def th(it):
    try: return it,Image.open(io.BytesIO(get(it[1]))).convert("RGB")
    except Exception: return it,None
with ThreadPoolExecutor(12) as ex: res=[r for r in ex.map(th,items) if r[1]]
W,H=220,330; cols=8; rows=(len(res)+cols-1)//cols
S=Image.new("RGB",(cols*W,rows*(H+30)),"white"); d=ImageDraw.Draw(S)
idx={}
for i,(it,im) in enumerate(res):
    im.thumbnail((W,H)); x,y=(i%cols)*W,(i//cols)*(H+30)
    S.paste(im,(x,y)); d.text((x+3,y+H+3),f"{i} {'USED ' if it[2] else ''}{it[0][:28]}",fill="red" if it[2] else "black")
    idx[i]=it[0]
S.save(f"{OUT}/sheet_{name}.jpg",quality=80)
json.dump(idx,open(f"{OUT}/sheet_{name}.json","w"),ensure_ascii=False,indent=0)
print(name,len(res))
