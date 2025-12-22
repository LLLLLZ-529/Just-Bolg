from graphviz import Digraph

def create_project_graph():
    dot = Digraph(
        'Just_Blog_Structure',
        comment='Just Blog Project Structure',
        format='png'
    )

    # ================= 全局布局 =================
    dot.attr(
        rankdir='TB',
        splines='curved',
        nodesep='0.3',
        ranksep='0.4',
        bgcolor='white',
        fontname='SimHei'
    )

    # ================= 默认节点样式 =================
    dot.attr(
        'node',
        shape='rect',
        style='filled,rounded',
        fontname='SimHei',
        fontsize='14',
        margin='0.2,0.1'
    )

    dot.attr(
        'edge',
        arrowsize='0.7',
        color='#546E7A',
        fontname='SimHei',
        fontsize='12'
    )

    # ================= 项目入口层 =================
    dot.node(
        'Root',
        'Just Blog\n项目根目录',
        fillcolor='#E3F2FD',
        color='#1565C0',
        fontcolor='#0D47A1',
        fontsize='16',
        penwidth='2'
    )

    dot.node(
        'Manage',
        'manage.py\n项目启动入口',
        fillcolor='#F5F5F5',
        color='#9E9E9E'
    )

    dot.edge('Root', 'Manage')

    # ================= 项目配置层 =================
    with dot.subgraph(name='cluster_config') as c:
        c.attr(
            label='项目配置层',
            fontsize='15',
            fontcolor='#37474F',
            style='rounded',
            color='#90A4AE',
            fontname='SimHei'
        )

        c.node('Settings', 'settings.py\n全局配置')
        c.node('RootUrls', 'urls.py\n总路由')

        c.edge('Settings', 'RootUrls')

    dot.edge('Root', 'Settings')

    # ================= 应用逻辑层 =================
    with dot.subgraph(name='cluster_app') as c:
        c.attr(
            label='应用逻辑层（blogs）',
            fontsize='15',
            fontcolor='#37474F',
            style='rounded',
            color='#81C784',
            fontname='SimHei'
        )

        c.node(
            'Models',
            'models.py\n数据模型',
            fillcolor='#FFFDE7',
            color='#FBC02D'
        )
        c.node(
            'Forms',
            'forms.py\n表单校验',
            fillcolor='#FFFDE7',
            color='#FBC02D'
        )
        c.node(
            'Views',
            'views.py\n业务逻辑与权限',
            fillcolor='#FFFDE7',
            color='#FBC02D'
        )
        c.node(
            'AppUrls',
            'urls.py\n应用路由',
            fillcolor='#F5F5F5',
            color='#BDBDBD'
        )

        c.edge('Models', 'Forms')
        c.edge('Forms', 'Views')
        c.edge('Views', 'AppUrls')

    dot.edge('RootUrls', 'AppUrls')

    # ================= 前端展示层 =================
    with dot.subgraph(name='cluster_frontend') as c:
        c.attr(
            label='前端展示层（Templates）',
            fontsize='15',
            fontcolor='#37474F',
            style='rounded',
            color='#64B5F6',
            fontname='SimHei'
        )

        c.node('Templates', 'templates/\nHTML 模板')
        c.node('Base', 'base.html\n页面骨架')
        c.node('Index', 'index.html\n文章列表')
        c.node('Detail', 'post_detail.html\n文章详情')
        c.node('Form', 'post_form.html\n发布 / 编辑')

        c.edge('Templates', 'Base')
        c.edge('Templates', 'Index')
        c.edge('Templates', 'Detail')
        c.edge('Templates', 'Form')

    dot.edge('Views', 'Templates')

    # ================= 资源管理层 =================
    with dot.subgraph(name='cluster_resource') as c:
        c.attr(
            label='资源管理层',
            fontsize='15',
            fontcolor='#37474F',
            style='rounded',
            color='#B0BEC5',
            fontname='SimHei'
        )

        c.node(
            'Static',
            'static/\nCSS / JS / 前端资源',
            fillcolor='#ECEFF1',
            color='#90A4AE'
        )
        c.node(
            'Media',
            'media/\n用户上传图片',
            fillcolor='#ECEFF1',
            color='#90A4AE'
        )

    dot.edge('Root', 'Static')
    dot.edge('Root', 'Media')

    # ================= 逻辑数据流（虚线） =================
    dot.attr(
        'edge',
        style='dashed',
        color='#EF5350',
        penwidth='1.4',
        constraint='false'
    )

    dot.edge('Models', 'Forms', xlabel='数据结构')
    dot.edge('Forms', 'Views', xlabel='数据校验')
    dot.edge('Views', 'Templates', xlabel='页面渲染')

    return dot


if __name__ == '__main__':
    g = create_project_graph()
    print(g.source)
    g.render('just_blog_structure', view=True, cleanup=True)
