#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", page_icon="🍀")
st.title("Welcome to My Growth Mindset Challenge!")

st.header("✨Embrace your Journey of Growth!")
st.write("Growth, at its core, signifies an increase or expansion in size, complexity, or development, encompassing both physical and metaphorical advancements. It's a process of becoming larger, stronger, or more mature, whether it's a plant reaching for the sun or a person pursuing their potential. ")

#quote section
st.header("🚀Inspirational quotes about growth")
st.write("“When we’re growing up there are all sorts of people telling us what to do when really what we need is space to work out who to be🎯” - Elliot Page")

st.header("✍What's Obstacle are you facing Today?")
user_input = st.text_input("Share a difficulty you're currently experiencing:")

#condition
if user_input:
    st.success(f"💪🏼you're encountering: {user_input}. Recognizing that you are not where you want to be is a starting point to begin changing your life. keep pushin forward!🚀")
else:
    st.warning("Share the difficulties you faced, when getting started!")

#relexing
st.header("🧠Think about what you'hv learned")
reflection= st.text_area("Share your thougths here:")

if reflection:
    st.success(f"Valuable perspective: your thoughts:{reflection}")
else:
    st.info("Looking back on past experience helps you grow! Tell about your Challenges")

#achievements
st.header("🏆Acknowledge your achievements")  
achievement= st.text_area("Talk about a recent achievement:")

if achievement:
    st.success(f"🥇Incredible! you accomplished it: {achievement}")
else:
    st.info("Every accomplishment matters, no matter the size! Share your now!🤩")    

            #footer
st.write("- - -")
st.write(" 🍀To accomplish great things, we must not only act, but also dream; not only plan, but also believe.")
st.write("**©Created by Rida Danish🌸**")

    
            
            

