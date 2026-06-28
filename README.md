# CAS-Materials-Computing-Platform

## 概要 / Overview

这是一款由中科院过程工程研究所小组开发的 Web 应用，致力于搭建适用于国内材料计算研究与工程应用的材料计算平台。

This is a web application developed by a research group from the Institute of Process Engineering, Chinese Academy of Sciences. The project aims to build a materials computing platform for domestic research and engineering use. 

## 环境说明 / Environment

本项目基于 **Python Flask Web 开发环境** 构建，主要技术栈如下：

- **后端框架**：Flask
- **数据库**：MySQL
- **ORM 框架**：Flask-SQLAlchemy
- **数据库迁移**：Flask-Migrate
- **邮件服务**：Flask-Mail，使用 QQ 邮箱 SMTP 服务
- **前端结构**：Flask Templates 模板渲染 + Static 静态资源
- **项目结构**：采用 Blueprint 蓝图方式组织路由模块

数据库连接使用 `mysql+pymysql`，默认连接本地 MySQL 服务，端口为 `3306`。项目通过 `config.py` 管理数据库、邮箱和应用密钥等配置信息。

主要依赖包括：

```text
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Mail
PyMySQL
```

This project is built on a **Python Flask Web development environment**. The main technical stack includes:

- **Backend framework**: Flask
- **Database**: MySQL
- **ORM framework**: Flask-SQLAlchemy
- **Database migration**: Flask-Migrate
- **Email service**: Flask-Mail with QQ Mail SMTP service
- **Frontend structure**: Flask Templates + Static resources
- **Project structure**: Blueprint-based route organization

The database connection uses `mysql+pymysql` and connects to a local MySQL service by default on port `3306`. The project uses `config.py` to manage database settings, email settings, and application secret keys.

Main dependencies include:

```text
Flask
Flask-SQLAlchemy
Flask-Migrate
Flask-Mail
PyMySQL
```

## 功能说明 / Features

本项目旨在提供一个面向材料计算与材料数据管理的 Web 平台，为热化学数据、参数数据和相关计算结果提供统一的管理、展示与查询入口。

This project aims to provide a web-based platform for materials computing and materials data management. It offers a unified entry for managing, displaying, and querying thermochemical data, parameter data, and related computing results.

目前项目已实现或规划的主要功能包括：

The current or planned features include:

1. **用户数据管理 / User Data Management**  
   项目定义了用户数据模型，可用于后续实现用户注册、登录、身份管理等功能。用户信息包括用户名、密码、邮箱和注册时间。  
   The project defines a user data model that can support future user registration, login, identity management, and account-related functions. User information includes username, password, email, and registration time.

2. **材料热化学数据管理 / Thermochemical Data Management**  
   项目设计了热化学数据表，用于存储材料或化学反应相关的热化学数据，包括名称、原始分子式、结果分子式、数据类型、物理量、数值、单位、计算或实验方法、参考文献、备注和标签等信息。  
   The project defines a thermochemical data model for storing materials or chemical reaction data, including name, original formula, result formula, data type, quantity, value, unit, method, reference, comments, and labels.

3. **参数数据管理 / Parameter Data Management**  
   项目设计了参数数据表，用于存储材料计算中可能用到的经验参数或拟合参数，包括温度范围、A-H 参数、参考文献、备注和标签等信息。  
   The project defines a parameter data model for storing empirical or fitted parameters used in materials computing, including temperature range, A-H parameters, reference, comments, and labels.

4. **数据关联与查询基础 / Data Relationship and Query Foundation**  
   参数数据表与热化学数据表之间通过分子式字段建立关联，为后续实现材料数据查询、筛选、对比和计算提供数据基础。  
   The parameter data model is associated with the thermochemical data model through formula fields, providing a foundation for future data query, filtering, comparison, and calculation functions.

5. **页面展示功能 / Page Rendering**  
   项目采用 Flask Templates 模板渲染方式，通过 `templates` 目录组织前端页面，并通过 `static` 目录管理 CSS、JavaScript、图片等静态资源。目前已通过 Blueprint 蓝图方式实现测试页面路由。  
   The project uses Flask Templates for page rendering and uses the `static` directory to manage CSS, JavaScript, images, and other static resources. A test page route has been organized through Flask Blueprint.

6. **邮件功能支持 / Email Service Support**  
   项目集成 Flask-Mail，可用于后续实现邮箱验证、通知发送、密码找回等功能。  
   Flask-Mail is integrated into the project and can support future email verification, notification sending, and password recovery functions.

7. **模块化开发结构 / Modular Development Structure**  
   项目将数据库扩展、邮件扩展、配置文件、数据模型和蓝图路由拆分到不同文件中，便于后续功能扩展和团队协作开发。  
   The project separates database extensions, mail extensions, configuration, data models, and blueprint routes into different modules, making the system easier to extend, maintain, and collaborate on.


