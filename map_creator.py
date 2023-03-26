import re
import sys
from bs4 import BeautifulSoup, NavigableString
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


s = None
html = ""
address = ""
elements = []
attr_count = {}

attr_id = "id"
unique_elements = []
repeated_elements = {}
no_identifier_elements = []


def lookup(link: str):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("excludeSwitches", ["enable-logging"])
    opt.add_argument("--disable-gpu")
    service = ChromeService(executable_path=".\\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=opt)
    global address
    address = link
    driver.get(link)
    global html
    html = driver.page_source
    global s
    s = BeautifulSoup(html, features="html.parser")
    rec(s)
    driver.quit()


def check_unique(value):
    return True if html.count(f'{attr_id}="{value}"') == 1 else False


def on_repeated_identifier(elem):
    repeated_elements[elem] = attr_id


def on_no_attribute(elem):
    no_identifier_elements.append(elem)


def find_identifier(elem):
    has_attr = False
    attributes = elem.attrs
    for k, v in attributes.items():
        if k == attr_id:
            if k == 'class':
                v1 = ""
                for i in range(len(v)):
                    v1 = v1 + v[i]
                v = v1
            has_attr = True
            if check_unique(v):
                unique_elements.append(elem)
            else:
                on_repeated_identifier(elem)
            break
    if not has_attr:
        on_no_attribute(elem)


# dfs algorithm
def rec(element):
    if len(element.findAll()) == 0:
        # print(element)
        return element
    for children in element.children:
        if isinstance(children, NavigableString):
            continue
        elem = rec(children)
        find_identifier(elem)
    return element


def set_identifier(identifier):
    global attr_id
    attr_id = identifier

def search_and_create(link, identifier, name, mode="w"):
    set_identifier(identifier)
    lookup(link)
    create_mapper(name, mode)


def create_mapper(name: str, mode):
    f = open(name + ".py", mode)
    if mode != "a":
        f.write(f"from selenium.webdriver.common.by import By\n")
        f.write(f"# this is a mapper for page: {address}\n")
        x = name.split('\\')[-1].capitalize()
        f.write(f"class {x}:\n")
        f.write("\n")
        f.write("\tdef __init__(self, sd):\n\t\tself.sd = sd\n\n")
    for elem in unique_elements:
        attr_value = elem.get(attr_id, default="oops")
        if attr_id == 'class':
            if len(attr_value) == 0:
                continue
            attr_value = attr_value[0]
        st = f"\"//*[@{attr_id}='{attr_value}']\""
        if elem.has_attr("name"):
            function_name = elem.get("name")
        else:
            function_name = attr_value
        function_name = re.sub("[-/@#%^&()!`~?><=+*']", "_", function_name)
        function_name = function_name.replace('-', '_').replace("/", "_")
        if elem.get("type") is not None:
            function_name = function_name + "_" + "_" + elem.get("type")
        else:
            function_name = function_name + "_" + elem.name
        f.write(f"\tdef {function_name}(self):\n\t\treturn self.sd.get_element({st}, 'xpath')")
        f.write("\n\n")
    f.close()

search_and_create("https://my-learning.w3schools.com/", "id", (sys.argv[1:])[0], "w")
search_and_create("https://my-learning.w3schools.com/", "class", (sys.argv[1:])[0], "a")

# time.sleep(4)
# search_and_create("http://128.90.13.104:8084/ows-mmr", "class", "login", "a")