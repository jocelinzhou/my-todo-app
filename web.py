import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip() #提取输入框中的内容用st.session_state
    if todo:
        todos.append(todo+"\n")
        functions.write_todos(todos)
    st.session_state['new_todo'] = " " #press enter后，输入框恢复空白


st.title("My todo App")
st.subheader("Need to do:")
    #st.write("Imporving  your productivity")

for index,todo in enumerate(todos):
    checked = st.checkbox(todo, key=todo)#此处key= todolist是指每一条的内容自己作为自己的id，不被重复
    if checked:
        todos.pop(index) #remove选中的。pop和remove的区别：pop（index），remove（具体指定的对象）
        functions.write_todos(todos) #重写 todolist
        del st.session_state[todo] #将选中的从页面显示上取出。与pop的区别，pop是从txt中去处
        st.rerun() #refresh the interface so that the completed task immediately disappears from Column 1 and appears in Column 2.


st.text_input(label="", placeholder="Enter a to do",
                  on_change=add_todo, key='new_todo') #on_change 跟def,trigger callback on enter， key类似id

