''' 我的主页 '''
import streamlit as st
from PIL import Image
page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智能词典","我的留言区"])

def page_1():
    ''' 我的兴趣推荐 '''
    with open('明天地球要爆炸（The Doomsday night）.mp3','rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.jpg')
    st.write('关于sdfj')
    st.write('众所周知，sdfj这个ggs是一个专门培养养成系男团的公司，旗下有四代，一代TFBOYS, 二代TNT时代少年团，TF家族三代登陆计划，TF家族四代练习生')
    st.write('')

    # 图片处理
    imgs_name_lst = ['一代.jpg', '二代.jpg', '三代.jpg', '四代.jpg']
    imgs_lst = []
    for i in imgs_name_lst:
        img = Image.open(i)
        img = img.resize((400, 300))
        imgs_lst.append(img)

    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.image(imgs_lst[0])
        st.write('TFBOYS')
        st.write('成员：凯、源、玺')
    with col2:
        st.image(imgs_lst[1])
        st.write('TNT时代少年团')
        st.write('成员：祺、鑫、轩、文、源、翔、霖')
    with col3:
        st.image(imgs_lst[2])
        st.write('TF家族三代登陆计划')
        st.write('成员：朱、禹、极、航、苏、豪、涵、丞、润、坤、邓、朔')
    with col4:
        st.image(imgs_lst[3])
        st.write('TF家族四代练习生')
        st.write('成员：官、熙、桂、瑞、杰、森、奇、文、博、然、宸、铭、智')

def page_2():
    ''' 我的图片处理工具 '''
    st.write(":clown_face:图片处理小程序:clown_face:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        # st.image(img)
        # st.image(img_change(img, 0, 2, 1))
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, 0, 2, 1))
        with tab3:
            st.image(img_change(img, 1, 2, 0))
        with tab4:
            st.image(img_change(img, 1, 0, 2))

def page_3():
    ''' 我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数: ', times_dict[n])
        if word == 'python':
            st.code('''
                    #  恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        if word == 'snow' or word == 'winter':
            st.snow()
        if word == 'birthday':
            st.balloons()

def page_4():
    ''' 我的留言区 '''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌧️'):
                st.write(i[1], ':',i[2])
        elif i [1] == '编程猫':
            with st.chat_message('🌯'):
                st.write(i[1], ':',i[2])
    name = st.selectbox('我是......', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i [0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()