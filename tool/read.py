import configparser
import os
import yaml

# data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
from ospath import yam_path, ini_path, switch_ini,middleground


class IniRead:
    # 初始化库
    def __init__(self, filename_, encoding='utf-8'):
        self.filename_ = filename_
        self.encoding_ = encoding
        self.conf_ = configparser.ConfigParser()

        if os.path.exists(filename_):
            try:
                self.red_conf = self.conf_.read(self.filename_, encoding=encoding)
            except Exception as e:
                raise print("加载配置文件出错：%s" % e)
        else:
            pass

    # 写入数据至ini
    def write_ini(self, section, option, value):
        section_list = self.conf_.sections()
        if section not in section_list:
            self.conf_.add_section(section)
            self.conf_.set(section, option, value)
        else:
            self.conf_.set(section, option, value)

        try:
            with open(self.filename_, "w+") as f:
                self.conf_.write(f)
        except FileNotFoundError as e:
            print("写入配置文件错误: %s" % e)
            raise e

    # 读取ini中的str类型数据
    def red_get(self, section, option):
        return self.conf_.get(section, option)

    # 读取ini中的int类型数据
    def red_int(self, section, option):
        return self.conf_.getint(section, option)

    # 读取ini中的布尔值，就是true和false
    def red_boolean(self, section, option):
        return self.conf_.getboolean(section, option)


class YamlRed:
    def __init__(self, filename_, encoding='utf-8'):

        self.filename_ = filename_
        self.encoding_ = encoding

        if os.path.exists(filename_):
            try:
                self.file_ = open(filename_, encoding=encoding)
            except Exception as e:
                raise print("加载yaml文件出错：%s" % e)
        else:
            pass

    def yaml_data(self):
        return yaml.safe_load(self.file_)

    # 写的这个需要的时候在优化
    def taml_write(self, _data):
        return yaml.dump(_data, self.file_)


red_data = YamlRed(middleground).yaml_data()
test_host = IniRead(ini_path).red_get("host", "api_sit_url")
yufa_host = IniRead(ini_path).red_get('credit_host', 'api_mex_test')
middleground_conf = IniRead(ini_path).red_get('middleground_host', 'api_middleground_test')
# release_host = IniRead(ini_path).red_get('host', 'api_mex_release')
if __name__ == '__main__':
    print(middleground_conf)
