BLOG_WORD(){
    # run the python file
    cd ~/Hodgepodge/Blog-word-counting
    /home/xiyuanyang/anaconda3/bin/python ~/Hodgepodge/Blog-word-counting/main.py;
    cat ~/Hodgepodge/Blog-word-counting/total.json | tail -5 | head -3
    echo "\nDone!"
    cd -
}
