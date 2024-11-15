from PackageA import *

package_api("r", "data.txt")
package_api("w", "data.txt", "哦！")


"""

软件包加密/混淆
pip install -U pyarmor
pyarmor gen -O dist1 -i /package_path

使用文档
https://pyarmor.readthedocs.io/zh/stable/part-1.html

"""