# 动画详解 SVG SMIL animation 以及 CSS 动画设置相关联系和区别, 用法

## 文件说明:
 - **test_leida** 有关雷达图的相关描述和CSS示例
 - **test_svg** 关于svg基础和动画的有关示例

## SVG 相关开发说明

'''
\<svg xmlns="" version="1.1">
    添加画图内容
\</svg>
'''
### CSS animation 
> 略

### SVG animations 描述
http://www.zhangxinxu.com/wordpress/2014/08/so-powerful-svg-smil-animation/

> -  **animation 的 begin() 可以设置按钮和按键等操作。**
> - **path可以设置到JS里面去, 其中stroke-dasharray, stroke-dashoffset需要关注**

    path {
      stroke-dasharray: 3000;
      stroke-dashoffset: 3000;
      -webkit-animation: dash 5s linear infinite;
      animation: dash 5s linear infinite;
    }
    
    css
        stroke-dasharray代表虚线之间的间距大小
        stroke-dashoffse代表虚线的偏移量
