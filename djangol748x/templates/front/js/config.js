
var projectName = '疫情数据可视化分析系统';
/**
 * 轮播图配置
 */
var swiper = {
	// 设定轮播容器宽度，支持像素和百分比
	width: '100%',
	height: '400px',
	// hover（悬停显示）
	// always（始终显示）
	// none（始终不显示）
	arrow: 'none',
	// default（左右切换）
	// updown（上下切换）
	// fade（渐隐渐显切换）
	anim: 'default',
	// 自动切换的时间间隔
	// 默认3000
	interval: 2000,
	// 指示器位置
	// inside（容器内部）
	// outside（容器外部）
	// none（不显示）
	indicator: 'outside'
}

/**
 * 个人中心菜单
 */
var centerMenu = [{
	name: '个人中心',
	url: '../' + localStorage.getItem('userTable') + '/center.html'
}, 
]


var indexNav = [

{
	name: '疫情信息',
	url: './pages/yiqingxinxi/list.html'
}, 
{
	name: '核酸检测',
	url: './pages/hesuanjiance/list.html'
}, 

{
	name: '新闻资讯',
	url: './pages/news/list.html'
},
]

var adminurl =  "http://localhost:8080/djangol748x/admin/dist/index.html";

var cartFlag = false

var chatFlag = false




var menu = [{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-present","buttons":["新增","查看","修改","删除"],"menu":"用户","menuJump":"列表","tableName":"yonghu"}],"menu":"用户管理"},{"child":[{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"员工","menuJump":"列表","tableName":"yuangong"}],"menu":"员工管理"},{"child":[{"appFrontIcon":"cuIcon-qrcode","buttons":["新增","查看","修改","删除"],"menu":"疫情信息","menuJump":"列表","tableName":"yiqingxinxi"}],"menu":"疫情信息管理"},{"child":[{"appFrontIcon":"cuIcon-camera","buttons":["查看","修改","删除"],"menu":"核酸检测","menuJump":"列表","tableName":"hesuanjiance"}],"menu":"核酸检测管理"},{"child":[{"appFrontIcon":"cuIcon-shop","buttons":["查看","修改","删除"],"menu":"检测预约","menuJump":"列表","tableName":"jianceyuyue"}],"menu":"检测预约管理"},{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["查看","修改","删除"],"menu":"检测结果","menuJump":"列表","tableName":"jiancejieguo"}],"menu":"检测结果管理"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看","修改","删除","审核"],"menu":"行程信息","menuJump":"列表","tableName":"xingchengxinxi"}],"menu":"行程信息管理"},{"child":[{"appFrontIcon":"cuIcon-present","buttons":["查看","修改","删除"],"menu":"轮播图管理","tableName":"config"},{"appFrontIcon":"cuIcon-news","buttons":["新增","查看","修改","删除"],"menu":"新闻资讯","tableName":"news"}],"menu":"系统管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看"],"menu":"疫情信息列表","menuJump":"列表","tableName":"yiqingxinxi"}],"menu":"疫情信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看","预约"],"menu":"核酸检测列表","menuJump":"列表","tableName":"hesuanjiance"}],"menu":"核酸检测模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"管理员","tableName":"users"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-shop","buttons":["查看","修改","删除"],"menu":"检测预约","menuJump":"列表","tableName":"jianceyuyue"}],"menu":"检测预约管理"},{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["查看"],"menu":"检测结果","menuJump":"列表","tableName":"jiancejieguo"}],"menu":"检测结果管理"},{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["新增","查看","修改","删除"],"menu":"行程信息","menuJump":"列表","tableName":"xingchengxinxi"}],"menu":"行程信息管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看"],"menu":"疫情信息列表","menuJump":"列表","tableName":"yiqingxinxi"}],"menu":"疫情信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看","预约"],"menu":"核酸检测列表","menuJump":"列表","tableName":"hesuanjiance"}],"menu":"核酸检测模块"}],"hasBackLogin":"是","hasBackRegister":"否","hasFrontLogin":"是","hasFrontRegister":"是","roleName":"用户","tableName":"yonghu"},{"backMenu":[{"child":[{"appFrontIcon":"cuIcon-camera","buttons":["新增","查看","修改","删除"],"menu":"核酸检测","menuJump":"列表","tableName":"hesuanjiance"}],"menu":"核酸检测管理"},{"child":[{"appFrontIcon":"cuIcon-shop","buttons":["查看","审核","检测结果"],"menu":"检测预约","menuJump":"列表","tableName":"jianceyuyue"}],"menu":"检测预约管理"},{"child":[{"appFrontIcon":"cuIcon-rank","buttons":["查看","修改","删除"],"menu":"检测结果","menuJump":"列表","tableName":"jiancejieguo"}],"menu":"检测结果管理"}],"frontMenu":[{"child":[{"appFrontIcon":"cuIcon-vipcard","buttons":["查看"],"menu":"疫情信息列表","menuJump":"列表","tableName":"yiqingxinxi"}],"menu":"疫情信息模块"},{"child":[{"appFrontIcon":"cuIcon-form","buttons":["查看","预约"],"menu":"核酸检测列表","menuJump":"列表","tableName":"hesuanjiance"}],"menu":"核酸检测模块"}],"hasBackLogin":"是","hasBackRegister":"是","hasFrontLogin":"否","hasFrontRegister":"否","roleName":"员工","tableName":"yuangong"}]


var isAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].backMenu.length;j++){
                for(let k=0;k<menus[i].backMenu[j].child.length;k++){
                    if(tableName==menus[i].backMenu[j].child[k].tableName){
                        let buttons = menus[i].backMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}

var isFrontAuth = function (tableName,key) {
    let role = localStorage.getItem("userTable");
    let menus = menu;
    for(let i=0;i<menus.length;i++){
        if(menus[i].tableName==role){
            for(let j=0;j<menus[i].frontMenu.length;j++){
                for(let k=0;k<menus[i].frontMenu[j].child.length;k++){
                    if(tableName==menus[i].frontMenu[j].child[k].tableName){
                        let buttons = menus[i].frontMenu[j].child[k].buttons.join(',');
                        return buttons.indexOf(key) !== -1 || false
                    }
                }
            }
        }
    }
    return false;
}