''' 我的主页 '''
import streamlit as st
from PIL import Image
page=st.sidebar.radio("我的首页",["我的兴趣推荐","我的图片处理工具","我的智能词典","我的留言区"])

def page_1():
    ''' 我的兴趣推荐 '''
    with open('明天地球要爆炸.mp3','rb') as f:
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

    # 图片处理
    img_name_lst = ['棍.jpg', '宝.jpg', '极.jpg', '航.jpg', '铲.jpg']
    img_lst = []
    for i in img_name_lst:
        img = Image.open(i)
        img = img.resize((300, 300))
        img_lst.append(img)

    col5, col6, col7, col8, col9 = st.columns([1, 1, 1, 1, 1])
    with col5:
        st.image(img_lst[0])
        st.write('朱志鑫')
        st.write('朱志鑫：别名：朱山根，2005年11月19日出生于重庆，天蝎座，应援色：云朗环星，粉丝名：小鑫星，应援口号：社死天才朱志鑫，吹拉弹唱样样行')
    with col6:
        st.image(img_lst[1])
        st.write('张泽禹')
        st.write('张泽禹：别名：小宝，2007年4月30日出生于黑龙江哈尔滨，金牛座，应援色：茶白柏绿，粉丝名：小禹宙，应援口号：张家翩翩少年郎，泽然若光如宝藏')
    with col7:
        st.image(img_lst[2])
        st.write('张极')
        st.write('张极：别名：格里芬，2007年2月3日出生于江苏常州，水瓶座，应援色：迩迩曦桔，粉丝名：金桔，应援口号：王牌张极，登峰造极')
    with col8:
        st.image(img_lst[3])
        st.write('左航')
        st.write('左航：别名：航酱，2006年5月22日出生于重庆綦江，双子座，应援色：逐浪百川，粉丝名：right，应援口号：左肩披星唤梦醒，航程万里远飞行')
    with col9:
        st.image(img_lst[4])
        st.write('苏新皓')
        st.write('苏新皓：别名：帅帅，2007年1月12日出生于河南开封，摩羯座，应援色：山城曙光，粉丝名：信号灯，应援口号：嘉陵少年意气傲，山城曙光苏新皓')
        
        # 图片处理
    img_name_lst2 = ['桂.jpg', '瑞.jpg', '奇.jpg', '文.jpg', '铭.jpg']
    img_lst2 = []
    for i in img_name_lst2:
        img = Image.open(i)
        img = img.resize((300, 300))
        img_lst2.append(img)

    col10, col11, col12, col13, col14 = st.columns([1, 1, 1, 1, 1])
    with col10:
        st.image(img_lst2[0])
        st.write('张桂源')
        st.write('张桂源：别名：张龙眼，2009年5月11日出生于重庆，金牛座，四代ACE')
    with col11:
        st.image(img_lst2[1])
        st.write('张函瑞')
        st.write('张函瑞：别名：，2009年10月18日出生于重庆，天秤座，四代主唱')
    with col12:
        st.image(img_lst2[2])
        st.write('左奇函')
        st.write('左奇函：别名：Aiden，2010年3月19日生于湖南衡阳，双鱼座，四代rap担')
    with col13:
        st.image(img_lst2[3])
        st.write('杨博文')
        st.write('杨博文：别名：，2006年5月22日出生于北京，双子座，四代主舞')
    with col14:
        st.image(img_lst2[4])
        st.write('陈浚铭')
        st.write('陈浚铭：别名：陈太帅，2012年5月17日出生于重庆，金牛座，四代门面')

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