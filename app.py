import os
import uvicorn
from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from bson import ObjectId
from typing import Optional, List
import motor.motor_asyncio

app = FastAPI()
conn_str = "mongodb+srv://luca:Yguanna32@clusterromanoff-n6wkh.mongodb.net/test?authSource=admin&replicaSet=ClusterRomanOff-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true"

conn_str = "mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass&ssl=false"
conn_str = "mongodb://localhost:27017"

#client = motor.motor_asyncio.AsyncIOMotorClient(conn_str)
client = motor.motor_asyncio.AsyncIOMotorClient(conn_str,serverSelectionTimeoutMS=5000)


db = client["devices"]
myCollection = "students"
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class StudentModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    pid: str = Field(...)
    devicetype: str = Field(...)
    brand: str = Field(...)
    model: str = Field(...)
    version: str = Field(...)
    fccid: str = Field(...)
    availability: str = Field(...)
    whereavailable: str = Field(...)
    supportedsincecommit: str = Field(...)
    supportedsincerel: str = Field(...)
    supportedcurrentrel: str = Field(...)
    unsupported_functions: str = Field(...)
    target: str = Field(...)
    subtarget: str = Field(...)
    packagearchitecture: str = Field(...)
    bootloader: str = Field(...)
    cpu: str = Field(...)
    cpucores: str = Field(...)
    cpumhz: str = Field(...)
    flashmb: str = Field(...)
    rammb: str = Field(...)
    ethernet100mports: str = Field(...)
    ethernetgbitports: str = Field(...)
    switch: str = Field(...)
    vlan: str = Field(...)
    modem: str = Field(...)
    commentsnetworkports: str = Field(...)
    wlanhardware: str = Field(...)
    wlan24ghz: str = Field(...)
    wlan50ghz: str = Field(...)
    wlancomments: str = Field(...)
    wlandriver: str = Field(...)
    detachableantennas: str = Field(...)
    bluetooth: str = Field(...)
    usbports: str = Field(...)
    sataports: str = Field(...)
    commentsusbsataports: str = Field(...)
    videoports: str = Field(...)
    audioports: str = Field(...)
    phoneports: str = Field(...)
    commentsavports: str = Field(...)
    serial: str = Field(...)
    serialconnectionparameters: str = Field(...)
    jtag: str = Field(...)
    ledcount: str = Field(...)
    buttoncount: str = Field(...)
    gpios: str = Field(...)
    powersupply: str = Field(...)
    devicepage: str = Field(...)
    device_techdata: str = Field(...)
    owrt_forum_topic_url: str = Field(...)
    lede_forum_topic_url: str = Field(...)
    forumsearch: str = Field(...)
    gitsearch: str = Field(...)
    wikideviurl: str = Field(...)
    oemdevicehomepageurl: str = Field(...)
    firmwareoemstockurl: str = Field(...)
    firmwareopenwrtinstallurl: str = Field(...)
    firmwareopenwrtupgradeurl: str = Field(...)
    firmwareopenwrtsnapshotinstallurl: str = Field(...)
    firmwareopenwrtsnapshotupgradeurl: str = Field(...)
    installationmethods: str = Field(...)
    commentinstallation: str = Field(...)
    recoverymethods: str = Field(...)
    commentrecovery: str = Field(...)
    picture: str = Field(...)
    comments: str = Field(...)


    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "pid":"16132",
                "devicetype":"WiFi Router",
                "brand":"Arcadyan / Astoria",
                "model":"ARV7510PW",
                "version":"NULL",
                "fccid":"NULL",
                "availability":"unknown 2018",
                "whereavailable":"UNAVAILABLE",
                "supportedcurrentrel":"external image",
                "unsupported_functions":"NULL",
                "target":"lantiq",
                "subtarget":"xway",
                "packagearchitecture":"mips_24kc",
                "bootloader":"brnboot",
                "cpu":"Lantiq XWAY Danube",
                "cpucores":"2",
                "cpumhz":"333",
                "flashmb":"16",
                "rammb":"32",
                "ethernet100mports":"4",
                "ethernetgbitports":"-",
                "switch":"Infineon ADM6996I",
                "vlan":"UNAVAILABLE",
                "modem":"ADSL2+",
                "wlanhardware":"Ralink RT2860T",
                "wlan24ghz":"b/g/n",
                "wlan50ghz":"-",
                "wlandriver":"rt2800pci",
                "detachableantennas":"UNAVAILABLE",
                "bluetooth":"UNAVAILABLE",
                "usbports":"2x 2.0",
                "sataports":"UNAVAILABLE",
                "videoports":"UNAVAILABLE",
                "audioports":"UNAVAILABLE",
                "phoneports":"UNAVAILABLE",
                "serial":"Yes",
                "serialconnectionparameters":"UNAVAILABLE",
                "jtag":"Yes",
                "ledcount":"UNAVAILABLE",
                "buttoncount":"2",
                "gpios":"UNAVAILABLE",
                "powersupply":"UNAVAILABLE",
                "devicepage":"toh:arcadyan:arv7510pw",
                "device_techdata":"View/Edit data",
                "owrt_forum_topic_url":"NULL",
                "lede_forum_topic_url":"NULL",
                "forumsearch":"ARV7510PW",
                "gitsearch":"ARV7510PW",
                "wikideviurl":"NULL",
                "firmwareopenwrtinstallurl":"NULL",
                "firmwareopenwrtupgradeurl":"http://www.elisanet.fi/malaakso/misc/openwrt-lantiq-xway-ARV4510PW-squashfs.image",
                "firmwareopenwrtsnapshotinstallurl":"NULL",
                "firmwareopenwrtsnapshotupgradeurl":"NULL",
                "installationmethods":"NULL",
                "recoverymethods":"NULL",
                "picture":"media:example:genericrouter1.png"
                }
        }
    


class UpdateStudentModel(BaseModel):
    pid: Optional[str]
    devicetype: Optional[str]
    brand: Optional[str]
    model: Optional[str]
    version: Optional[str]
    fccid: Optional[str]
    availability: Optional[str]
    whereavailable: Optional[str]
    supportedsincecommit: Optional[str]
    supportedsincerel: Optional[str]
    supportedcurrentrel: Optional[str]
    unsupported_functions: Optional[str]
    target: Optional[str]
    subtarget: Optional[str]
    packagearchitecture: Optional[str]
    bootloader: Optional[str]
    cpu: Optional[str]
    cpucores: Optional[str]
    cpumhz: Optional[str]
    flashmb: Optional[str]
    rammb: Optional[str]
    ethernet100mports: Optional[str]
    ethernetgbitports: Optional[str]
    switch: Optional[str]
    vlan: Optional[str]
    modem: Optional[str]
    commentsnetworkports: Optional[str]
    wlanhardware: Optional[str]
    wlan24ghz: Optional[str]
    wlan50ghz: Optional[str]
    wlancomments: Optional[str]
    wlandriver: Optional[str]
    detachableantennas: Optional[str]
    bluetooth: Optional[str]
    usbports: Optional[str]
    sataports: Optional[str]
    commentsusbsataports: Optional[str]
    videoports: Optional[str]
    audioports: Optional[str]
    phoneports: Optional[str]
    commentsavports: Optional[str]
    serial: Optional[str]
    serialconnectionparameters: Optional[str]
    jtag: Optional[str]
    ledcount: Optional[str]
    buttoncount: Optional[str]
    gpios: Optional[str]
    powersupply: Optional[str]
    devicepage: Optional[str]
    device_techdata: Optional[str]
    owrt_forum_topic_url: Optional[str]
    lede_forum_topic_url: Optional[str]
    forumsearch: Optional[str]
    gitsearch: Optional[str]
    wikideviurl: Optional[str]
    oemdevicehomepageurl: Optional[str]
    firmwareoemstockurl: Optional[str]
    firmwareopenwrtinstallurl: Optional[str]
    firmwareopenwrtupgradeurl: Optional[str]
    firmwareopenwrtsnapshotinstallurl: Optional[str]
    firmwareopenwrtsnapshotupgradeurl: Optional[str]
    installationmethods: Optional[str]
    commentinstallation: Optional[str]
    recoverymethods: Optional[str]
    commentrecovery: Optional[str]
    picture: Optional[str]
    comments: Optional[str]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "pid":"16132",
                "devicetype":"WiFi Router",
                "brand":"Arcadyan / Astoria",
                "model":"ARV7510PW",
                "version":"NULL",
                "fccid":"NULL",
                "availability":"unknown 2018",
                "whereavailable":"UNAVAILABLE",
                "supportedcurrentrel":"external image",
                "unsupported_functions":"NULL",
                "target":"lantiq",
                "subtarget":"xway",
                "packagearchitecture":"mips_24kc",
                "bootloader":"brnboot",
                "cpu":"Lantiq XWAY Danube",
                "cpucores":"2",
                "cpumhz":"333",
                "flashmb":"16",
                "rammb":"32",
                "ethernet100mports":"4",
                "ethernetgbitports":"-",
                "switch":"Infineon ADM6996I",
                "vlan":"UNAVAILABLE",
                "modem":"ADSL2+",
                "wlanhardware":"Ralink RT2860T",
                "wlan24ghz":"b/g/n",
                "wlan50ghz":"-",
                "wlandriver":"rt2800pci",
                "detachableantennas":"UNAVAILABLE",
                "bluetooth":"UNAVAILABLE",
                "usbports":"2x 2.0",
                "sataports":"UNAVAILABLE",
                "videoports":"UNAVAILABLE",
                "audioports":"UNAVAILABLE",
                "phoneports":"UNAVAILABLE",
                "serial":"Yes",
                "serialconnectionparameters":"UNAVAILABLE",
                "jtag":"Yes",
                "ledcount":"UNAVAILABLE",
                "buttoncount":"2",
                "gpios":"UNAVAILABLE",
                "powersupply":"UNAVAILABLE",
                "devicepage":"toh:arcadyan:arv7510pw",
                "device_techdata":"View/Edit data",
                "owrt_forum_topic_url":"NULL",
                "lede_forum_topic_url":"NULL",
                "forumsearch":"ARV7510PW",
                "gitsearch":"ARV7510PW",
                "wikideviurl":"NULL",
                "firmwareopenwrtinstallurl":"NULL",
                "firmwareopenwrtupgradeurl":"http://www.elisanet.fi/malaakso/misc/openwrt-lantiq-xway-ARV4510PW-squashfs.image",
                "firmwareopenwrtsnapshotinstallurl":"NULL",
                "firmwareopenwrtsnapshotupgradeurl":"NULL",
                "installationmethods":"NULL",
                "recoverymethods":"NULL",
                "picture":"media:example:genericrouter1.png"
                }
        }


@app.post("/", response_description="Add new student", response_model=StudentModel)
async def create_student(student: StudentModel = Body(...)):
    student = jsonable_encoder(student)
    new_student = await db[myCollection].insert_one(student)
    created_student = await db[myCollection].find_one({"_id": new_student.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_student)


@app.get(
    "/", response_description="List all students", response_model=List[StudentModel]
)
async def list_students():

    async for doc in db[myCollection].find():
        print(doc)

    #students = await db[myCollection].findone().to_list(length=100)
    students = {}
    #students = await db[myCollection].find().to_list(length=100)
    return students


@app.get(
    "/{id}", response_description="Get a single student", response_model=StudentModel
)
async def show_student(id: str):
    if (student := await db[myCollection].find_one({"_id": id})) is not None:
        return student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.put("/{id}", response_description="Update a student", response_model=StudentModel)
async def update_student(id: str, student: UpdateStudentModel = Body(...)):
    student = {k: v for k, v in student.dict().items() if v is not None}

    if len(student) >= 1:
        update_result = await db[myCollection].update_one({"_id": id}, {"$set": student})

        if update_result.modified_count == 1:
            if (
                updated_student := await db[myCollection].find_one({"_id": id})
            ) is not None:
                return updated_student

    if (existing_student := await db[myCollection].find_one({"_id": id})) is not None:
        return existing_student

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


@app.delete("/{id}", response_description="Delete a student")
async def delete_student(id: str):
    delete_result = await db[myCollection].delete_one({"_id": id})

    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(status_code=404, detail=f"Student {id} not found")


if __name__ == '__main__':
    uvicorn.run(app, port=5000)