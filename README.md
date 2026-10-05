# 📝 Just Blog

基于 **Django 6** 的多用户博客应用：发布文章（支持配图）、评论互动、注册/登录，带完整的用户权限控制。

## ✨ 功能特性

- 📄 **文章发布**：标题 + 正文 + 可选配图（`BlogPost` 模型，图片存 `media/blog_images/`）
- 💬 **评论系统**：登录用户可评论，支持删除（作者本人或超管）
- ✏️ **编辑与删除**：文章作者可编辑/删除自己的文章（`edit_post` / `delete_post`）
- 🔐 **用户系统**：注册、登录、登出（Django 自带认证 + `UserCreationForm`）
- 🖼️ **图片上传**：`ImageField` 上传配图，`MEDIA_ROOT` 管理
- 🛡️ **权限控制**：非作者无法编辑/删除他人文章（`@login_required` + 归属校验）

## 🚀 快速开始

### 环境依赖

```bash
# Python 3.10+（Django 6.0）
pip install django pillow
```

### 运行

```bash
cd Blogs

# 1. 初始化数据库
python manage.py migrate

# 2. 创建管理员（可选，用于后台管理）
python manage.py createsuperuser

# 3. 启动
python manage.py runserver
```

打开 `http://127.0.0.1:8000/` 访问博客首页，`http://127.0.0.1:8000/admin` 进入 Django 后台。

## 📁 项目结构

```
Blogs/
├── manage.py          # Django 管理入口
├── Blog/              # 项目配置（settings / urls / wsgi / asgi）
├── blogs/             # 博客应用
│   ├── models.py      # BlogPost / Comment 模型
│   ├── views.py       # 首页、详情、发布、编辑、删除、评论、注册
│   ├── forms.py       # 文章与评论表单
│   ├── urls.py        # 应用路由
│   ├── admin.py       # 后台注册
│   ├── templates/     # HTML 模板（含登录注册页）
│   └── static/        # 样式
├── media/blog_images/ # 用户上传的配图
├── db.sqlite3         # ⚠️ 本地数据库（不应提交 git）
└── graph.py           # 额外脚本【待确认用途】
```

## 📄 许可

未指定开源许可（默认保留所有权利）。
