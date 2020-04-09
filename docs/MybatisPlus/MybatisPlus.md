## MybatisPlus

### MybatisPlus简介
- MybatisPlus简称MP， 是一个Mybatis的增强工具包，只做增强不做改变，为简化开发工作、提升效率而生
- 我们的愿景是成为Mybatis最好的搭档！

### 代码及文档发布地址
- [官网](https://mp.baomidou.com/)
- [官网参考文档](https://mp.baomidou.com/guide/)
- [github](https://github.com/baomidou/mybatis-plus)
- [码云](https://gitee.com/baomidou/mybatis-plus)

### 特性
- 无侵入：只做增强不做改变，引入它不会对现有工程产生影响，如丝般顺滑
- 损耗小：启动即会自动注入基本 CURD，性能基本无损耗，直接面向对象操作
- 强大的 CRUD 操作：内置通用 Mapper、通用 Service，仅仅通过少量配置即可实现单表大部分 CRUD 操作，更有强大的条件构造器，满足各类使用需求
- 支持 Lambda 形式调用：通过 Lambda 表达式，方便的编写各类查询条件，无需再担心字段写错
- 支持主键自动生成：支持多达 4 种主键策略（内含分布式唯一 ID 生成器 - Sequence），可自由配置，完美解决主键问题
- 支持 ActiveRecord 模式：支持 ActiveRecord 形式调用，实体类只需继承 Model 类即可进行强大的 CRUD 操作
- 支持自定义全局通用操作：支持全局通用方法注入（ Write once, use anywhere ）
- 内置代码生成器：采用代码或者 Maven 插件可快速生成 Mapper 、 Model 、 Service 、 Controller 层代码，支持模板引擎，更有超多自定义配置等您来使用
- 内置分页插件：基于 MyBatis 物理分页，开发者无需关心具体操作，配置好插件之后，写分页等同于普通 List 查询
- 分页插件支持多种数据库：支持 MySQL、MariaDB、Oracle、DB2、H2、HSQL、SQLite、Postgre、SQLServer 等多种数据库
- 内置性能分析插件：可输出 Sql 语句以及其执行时间，建议开发测试时启用该功能，能快速揪出慢查询
- 内置全局拦截插件：提供全表 delete 、 update 操作智能分析阻断，也可自定义拦截规则，预防误操作

### 安装
- Spring Boot
    ```xml
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus-boot-starter</artifactId>
        <version>3.3.1.tmp</version>
    </dependency>
    ```
- Spring MVC
    ```xml
    <dependency>
        <groupId>com.baomidou</groupId>
        <artifactId>mybatis-plus</artifactId>
        <version>3.3.1.tmp</version>
    </dependency>
    ```
> 引入 MyBatis-Plus 之后请不要再次引入 MyBatis 以及 MyBatis-Spring，以避免因版本差异导致的问题

### 配置
- Spring Boot 工程
    - 配置MapperScan 注解
        ```java
        @SpringBootApplication
        @MapperScan("com.baomidou.mybatisplus.samples.quickstart.mapper")
        public class Application {

            public static void main(String[] args) {
                SpringApplication.run(QuickStartApplication.class, args);
            }

        }
        ```
- Spring MVC 工程
    - 配置 MapperScan
        ```xml
        <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
            <property name="basePackage" value="com.baomidou.mybatisplus.samples.quickstart.mapper"/>
        </bean>
        ```
    - 调整 SqlSessionFactory 为 MyBatis-Plus 的 SqlSessionFactory
        ```xml
        <bean id="sqlSessionFactory" class="com.baomidou.mybatisplus.extension.spring.MybatisSqlSessionFactoryBean">
            <property name="dataSource" ref="dataSource"/>
        </bean>
        ```

### Mapper接口
- 基于Mybatis：在Mapper接口中编写CRUD相关的方法，提供Mapper接口所对应的SQL映射文件以及方法对应的SQL语句
- 基于MP：让XxxMapper接口继承BaseMapper接口即可，`BaseMapper<?>`泛型指定的就是当前Mapper接口所要操作的实体类的类型

    