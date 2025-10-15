'''
Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
 

Example 1:


Input
["FileSystem", "ls", "mkdir", "addContentToFile", "ls", "readContentFromFile"]
[[], ["/"], ["/a/b/c"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"]]
Output
[null, [], null, null, ["a"], "hello"]

Explanation
FileSystem fileSystem = new FileSystem();
fileSystem.ls("/");                         // return []
fileSystem.mkdir("/a/b/c");
fileSystem.addContentToFile("/a/b/c/d", "hello");
fileSystem.ls("/");                         // return ["a"]
fileSystem.readContentFromFile("/a/b/c/d"); // return "hello"
 

Constraints:

1 <= path.length, filePath.length <= 100
path and filePath are absolute paths which begin with '/' and do not end with '/' except that the path is just "/".
You can assume that all directory names and file names only contain lowercase letters, and the same names will not exist in the same directory.
You can assume that all operations will be passed valid parameters, and users will not attempt to retrieve file content or list a directory or file that does not exist.
You can assume that the parent directory for the file in addContentToFile will exist.
1 <= content.length <= 50
At most 300 calls will be made to ls, mkdir, addContentToFile, and readContentFromFile.
'''

from collections import defaultdict
from typing import List

class TrieNode:
    def __init__(self):
        self.is_file = False
        self.content = ""
        self.children = defaultdict(TrieNode)

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def ls(self, path: str) -> List[str]:
        cur = self.root
        for p in path.split('/'):
            if not p:
                continue
            cur = cur.children[p]
        if cur.is_file:
            return [p]
        else:
            ans = [file for file in cur.children.keys()]
            return sorted(ans) if ans else []

    def mkdir(self, path: str) -> None:
        cur = self.root
        for p in path.split('/'):
            if not p:
                continue
            cur = cur.children[p]

    def addContentToFile(self, filePath: str, content: str) -> None:
        cur = self.root
        for p in filePath.split('/'):
            if not p:
                continue
            cur = cur.children[p]
        cur.is_file = True
        cur.content += content

    def readContentFromFile(self, filePath: str) -> str:
        cur = self.root
        for p in filePath.split('/'):
            if not p:
                continue
            cur = cur.children[p]
        if cur.is_file:
            return cur.content
        return ""


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)