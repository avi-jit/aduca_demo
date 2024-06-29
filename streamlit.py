import streamlit as st
#import pandas as pd
import openai
import json
import os

gpt = openai.OpenAI(api_key=os.get_env("openai_api_key"))
st.write("""
# ADUCA Demo
## by Avijit Thawani
""")


prompt = """Given an object list the parts of the object, their affordances, and their disabling characteristic.

Respond in JSON only.

Example below:
object: bus
parts: wheel, door, window, mirror, steering wheel, seat, engine
affordance: "wheel": ["getting from one place to another","transport many people at once","turning","moving children to school"], "mirror": ["observe the road conditions behind you"], "seat":["carry passengers","seat capacity","transport many people at once"], "steering wheel":["turning"], "windows":["looking outside"], "door":["getting in and out of the bus"], "engine":["powering the bus"]
disable: "wheel": "flat","mirror": "dirty", "seat": "small", "steering wheel": "broken", "windows": "dirty", "door": "broken", "engine": "out of fuel"

object: """ + st.text_input("Enter an object, e.g., bus")

out = json.loads(gpt.chat.completions.create(
    model="gpt-4o",
    response_format={ "type": "json_object" },
    messages=[{"role": "user", "content": prompt}],
).choices[0].message.content)

# display the output
st.write(out)