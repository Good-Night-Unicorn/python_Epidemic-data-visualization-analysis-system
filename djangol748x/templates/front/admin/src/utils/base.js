const base = {
    get() {
        return {
            url : "http://localhost:8080/djangol748x/",
            name: "djangol748x",
            // 退出到首页链接
            indexUrl: 'http://localhost:8080/front/index.html'
        };
    },
    getProjectName(){
        return {
            projectName: "疫情数据可视化分析系统"
        } 
    }
}
export default base
