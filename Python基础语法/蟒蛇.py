import turtle
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)   # rad表示爬行圆形轨迹的半径位置，正值为左，负值为右，angle表示小乌龟爬行的弧度值
        turtle.circle(-rad,angle)
    turtle.circle(rad,angle/2)
    turtle.fd(rad)                      # forward简写，代表爬行的直线距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0) # 长度，高度，左上角坐标起始点
    pythonsize = 60            
    turtle.pensize(pythonsize) # 宽度，小乌龟宽度
    turtle.pencolor("black")   # 小乌龟走过的轨迹颜色
    turtle.seth(-40)           # 小乌龟开始爬行的角度方向，参照数学象限
    drawSnake(40,80,5,pythonsize/2) 
main()
