# claude

这个项目的目的是帮助Termux用户构建一个快捷方便的Claude终端。

声明：该仓库来源于[这个项目](https://github.com/yokonsan/claude-in-slack-api)。

## 准备环境

在主目录下运行`git clone git@github.com:14983/claude.git`，之后运行`claude/main.sh`。这个时候，您的`.bashrc`文件会被修改。

运行`pip install -r claude/requirements.txt`，稍等一会儿，运行环境就准备完成了！

您还需要在`.env`文件中填入Claude/Slack的Token，请在原项目中寻找查看方法。

## 运行！

每次启动Termux的时候，Claude会自动运行，蓝色的`->`代表您输入的信息，红色的`->`代表Claude输入的信息。