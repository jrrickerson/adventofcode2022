import solve
import utils


def test_parse_command_empty():
    lines = []

    cmd, output = utils.parse_command(lines)

    assert cmd is None
    assert output is None


def test_parse_command_invalid_command():
    lines = [
        "1234 hello.txt",
    ]

    cmd, output = utils.parse_command(lines)

    assert cmd is None
    assert output is None


def test_parse_command_no_args():
    lines = [
        "$ ls",
    ]

    cmd, output = utils.parse_command(lines)

    assert cmd == ("ls",)
    assert output == []


def test_parse_command_single_arg():
    lines = [
        "$ cd /",
    ]

    cmd, output = utils.parse_command(lines)

    assert cmd == ("cd", "/")
    assert output == []


def test_parse_command_multi_arg():
    lines = [
        "$ cp a b",
    ]

    cmd, output = utils.parse_command(lines)

    assert cmd == ("cp", "a", "b")
    assert output == []


def test_parse_command_with_output():
    lines = [
        "$ ls",
        "123 abc.txt",
        "456 def.dat",
    ]

    cmd, output = utils.parse_command(lines)

    assert cmd == ("ls",)
    assert output == [
        "123 abc.txt",
        "456 def.dat",
    ]


def test_parse_listing_empty():
    lines = []

    entries = utils.parse_listing(lines)

    assert entries == {}


def test_parse_listing_dirs_only():
    lines = [
        "dir a",
        "dir b",
        "dir c",
    ]

    entries = utils.parse_listing(lines)

    assert len(entries) == 3
    assert "a" in entries
    assert entries["a"] == {"__name__": "a"}
    assert "b" in entries
    assert entries["b"] == {"__name__": "b"}
    assert "c" in entries
    assert entries["c"] == {"__name__": "c"}


def test_parse_listing_files_only():
    lines = [
        "123 a.txt",
        "456 b.out",
        "890 c.dat",
    ]

    entries = utils.parse_listing(lines)

    assert len(entries) == 3
    assert entries["a.txt"] == 123
    assert entries["b.out"] == 456
    assert entries["c.dat"] == 890


def test_parse_listing_mixed_entries():
    lines = [
        "dir a",
        "123 b.txt",
        "456 c.out",
        "dir d",
        "dir e",
        "890 f.dat",
    ]

    entries = utils.parse_listing(lines)

    assert len(entries) == 6
    assert entries["a"] == {"__name__": "a"}
    assert entries["d"] == {"__name__": "d"}
    assert entries["e"] == {"__name__": "e"}
    assert entries["b.txt"] == 123
    assert entries["c.out"] == 456
    assert entries["f.dat"] == 890


def test_attach_directory_empty():
    name = "testdir"
    parent = {}
    entries = {}

    newdir = utils.attach_directory(name, entries, parent)

    assert newdir[".."] is parent
    assert newdir["__name__"] == name
    assert parent[name] is newdir
    assert list(newdir.keys()) == ["..", "__name__"]


def test_attach_directory_root():
    name = "/"
    parent = {
        "__name__": "/",
    }
    entries = {
        "a.out": 123,
        "b.txt": 456,
        "subdir1": {},
        "subdir2": {},
    }

    newdir = utils.attach_directory(name, entries, parent)

    assert newdir["__name__"] == name
    assert newdir[".."] is newdir
    for key, value in entries.items():
        assert newdir[key] == value


def test_attach_directory_update_existing_entry():
    name = "testdir"
    parent = {
        "abc": {},
        "xyz": {},
        "testdir": {},
    }
    entries = {}

    newdir = utils.attach_directory(name, entries, parent)

    assert newdir[".."] is parent
    assert newdir["__name__"] == name
    assert parent[name] is newdir
    assert list(newdir.keys()) == ["..", "__name__"]


def test_attach_directory_with_entries():
    name = "testdir"
    parent = {
        "abc": {},
        "xyz": {},
    }
    entries = {
        "a.out": 123,
        "b.txt": 456,
        "subdir1": {},
        "subdir2": {},
    }

    newdir = utils.attach_directory(name, entries, parent)

    assert parent[name] is newdir
    assert newdir[".."] is parent
    assert newdir["__name__"] == name
    for key, value in entries.items():
        assert newdir[key] == value


def test_handle_change_directory_to_root():
    root = {
        "__name__": "/",
        "testdir": {
            "__name__": "testdir",
            "abc.txt": 123,
            "def.dat": 456,
        },
    }
    root["testdir"][".."] = root
    cwd = root["testdir"]
    path_stack = [root, cwd]
    dirname = "/"
    output = []

    cwd = utils.handle_change_directory(
        dirname, cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert cwd is root


def test_handle_change_directory_to_subdir():
    root = {
        "__name__": "/",
        "testdir": {
            "__name__": "testdir",
            "abc.txt": 123,
            "def.dat": 456,
            "subdir": {},
        },
    }
    root["testdir"][".."] = root
    cwd = root["testdir"]
    path_stack = [root, cwd]
    dirname = "subdir"
    output = []

    cwd = utils.handle_change_directory(
        dirname, cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert cwd is root["testdir"]["subdir"]


def test_handle_change_directory_to_parent():
    root = {
        "__name__": "/",
        "testdir": {
            "__name__": "testdir",
            "abc.txt": 123,
            "def.dat": 456,
            "subdir": {
                "__name__": "subdir",
            },
        },
    }
    root["testdir"][".."] = root
    root["testdir"]["subdir"][".."] = root["testdir"]
    cwd = root["testdir"]["subdir"]
    path_stack = [root, root["testdir"], cwd]
    dirname = ".."
    output = []

    cwd = utils.handle_change_directory(
        dirname, cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert cwd is root["testdir"]


def test_handle_change_directory_to_invalid_subdir():
    root = {
        "__name__": "/",
        "testdir": {
            "__name__": "testdir",
            "abc.txt": 123,
            "def.dat": 456,
            "subdir": {},
        },
    }
    root["testdir"][".."] = root
    cwd = root["testdir"]
    path_stack = [root, cwd]
    dirname = "not_a_directory"
    output = []

    cwd = utils.handle_change_directory(
        dirname, cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert cwd is root["testdir"]


def test_handle_list_directory_root_no_entries():
    root = {
        "__name__": "/",
    }
    cwd = root
    path_stack = [root]
    output = []

    utils.handle_list_directory(
        cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert len(root.keys()) == 2
    assert "__name__" in root
    assert ".." in root


def test_handle_list_directory_root_with_entries():
    root = {
        "__name__": "/",
    }
    cwd = root
    path_stack = [root]
    output = [
        "123 abc.txt",
        "345 def.dat",
        "dir testdir",
    ]

    utils.handle_list_directory(
        cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert len(root.keys()) == 5
    assert "__name__" in root
    assert ".." in root
    assert root["abc.txt"] == 123
    assert root["def.dat"] == 345
    assert root["testdir"] == {"__name__": "testdir"}


def test_handle_list_directory_subdir_no_entries():
    root = {
        "__name__": "/",
        "testdir": {"__name__": "testdir"},
    }
    cwd = root["testdir"]
    path_stack = [root, cwd]
    output = []

    utils.handle_list_directory(
        cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert len(cwd.keys()) == 2
    assert cwd["__name__"] == "testdir"
    assert cwd[".."] is root


def test_handle_list_directory_subdir_with_entries():
    root = {
        "__name__": "/",
        "testdir": {"__name__": "testdir"},
    }
    cwd = root["testdir"]
    path_stack = [root, cwd]
    output = [
        "123 abc.txt",
        "345 def.dat",
        "dir otherdir",
    ]

    utils.handle_list_directory(
        cwd=cwd, root=root, path_stack=path_stack, output=output)

    assert len(cwd.keys()) == 5
    assert cwd["__name__"] == "testdir"
    assert cwd[".."] is root
    assert cwd["abc.txt"] == 123
    assert cwd["def.dat"] == 345
    assert cwd["otherdir"] == {"__name__": "otherdir"}


def test_create_directory_tree_root_only():
    input_lines = []

    dirtree = utils.create_directory_tree(input_lines)

    assert dirtree == {"__name__": "/"}


def test_create_directory_tree_root_with_files():
    input_lines = [
        "$ cd /",
        "$ ls",
        "123 abc.txt",
        "345 def.dat",
    ]

    dirtree = utils.create_directory_tree(input_lines)

    assert len(dirtree) == 4
    assert dirtree["__name__"] == "/"
    assert dirtree[".."] is dirtree
    assert dirtree["abc.txt"] == 123
    assert dirtree["def.dat"] == 345


def test_create_directory_tree_root_with_dirs():
    input_lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "dir b",
    ]

    dirtree = utils.create_directory_tree(input_lines)

    assert len(dirtree) == 4
    assert dirtree["__name__"] == "/"
    assert dirtree[".."] is dirtree
    assert dirtree["a"]["__name__"] == "a"
    assert dirtree["b"]["__name__"] == "b"


def test_create_directory_tree_with_single_subdir():
    input_lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "$ cd a",
        "$ ls",
        "123 abc.txt",
        "345 def.dat",
    ]

    dirtree = utils.create_directory_tree(input_lines)

    assert len(dirtree) == 3
    assert dirtree["__name__"] == "/"
    assert dirtree[".."] is dirtree
    assert dirtree["a"]["__name__"] == "a"
    assert dirtree["a"][".."] is dirtree
    assert dirtree["a"]["abc.txt"] == 123
    assert dirtree["a"]["def.dat"] == 345


def test_create_directory_tree_multiple_subdirs():
    input_lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "dir b",
        "$ cd a",
        "$ ls",
        "123 abc.txt",
        "345 def.dat",
        "$ cd ..",
        "$ cd b",
        "$ ls",
        "890 123.txt",
        "678 456.num",
    ]

    dirtree = utils.create_directory_tree(input_lines)

    print(list(dirtree.keys()))
    assert len(dirtree) == 4
    assert dirtree["__name__"] == "/"
    assert dirtree[".."] is dirtree

    print(list(dirtree["a"].keys()))
    assert dirtree["a"]["__name__"] == "a"
    assert dirtree["a"][".."] is dirtree
    assert dirtree["a"]["abc.txt"] == 123
    assert dirtree["a"]["def.dat"] == 345

    print(list(dirtree["b"].keys()))
    assert dirtree["b"]["__name__"] == "b"
    assert dirtree["b"][".."] is dirtree
    assert dirtree["b"]["123.txt"] == 890
    assert dirtree["b"]["456.num"] == 678


def test_create_directory_tree_nested_subdirs():
    input_lines = [
        "$ cd /",
        "$ ls",
        "dir a",
        "$ cd a",
        "$ ls",
        "dir b",
        "$ cd b",
        "$ ls",
        "dir c",
        "$ cd c",
        "$ ls",
        "dir d",
        "$ cd d",
        "$ ls",
        "dir e",
        "$ cd e",
        "$ ls",
        "dir f",
        "$ cd f",
        "$ ls",
        "123 abc.txt",
    ]

    dirtree = utils.create_directory_tree(input_lines)

    print(list(dirtree.keys()))
    assert len(dirtree) == 3
    assert dirtree["__name__"] == "/"
    assert dirtree[".."] is dirtree

    assert dirtree["a"]["b"]["c"]["d"]["e"]["f"]["abc.txt"] == 123
    assert (dirtree["a"]["b"]["c"]["d"]["e"]["f"][".."] is 
            dirtree["a"]["b"]["c"]["d"]["e"])

def test_find_directory_size_root_files():
    root = {
        "__name__": "/",
        "abc.txt": 123,
        "def.dat": 456,
    }

    sizes = {}
    total = utils.find_directory_sizes(
        root, root["__name__"], sizes=sizes)

    assert total == (123 + 456)
    assert sizes["/"] == (123 + 456)


def test_find_directory_size_root_files_empty_subdirs():
    root = {
        "__name__": "/",
        "abc.txt": 123,
        "def.dat": 456,
        "subdir1": {},
        "subdir2": {},
    }
    root[".."] = root

    sizes = {}
    total = utils.find_directory_sizes(
        root, root["__name__"], sizes=sizes)

    assert total == (123 + 456)
    assert sizes["/"] == (123 + 456)
    assert sizes["/subdir1/"] == 0
    assert sizes["/subdir2/"] == 0


def test_find_directory_size_subdir_files():
    root = {
        "__name__": "/",
        "abc.txt": 123,
        "def.dat": 456,
        "subdir1": {
            "__name__": "subdir1",
            "AAA.txt": 100,
            "BBB.txt": 200,
        },
        "subdir2": {
            "__name__": "subdir1",
            "CCC.txt": 300,
            "DDD.txt": 400,
        },
    }
    root[".."] = root
    root["subdir1"][".."] = root
    root["subdir2"][".."] = root

    sizes = {}
    total = utils.find_directory_sizes(
        root, root["__name__"], sizes=sizes)

    assert total == (123 + 456) + (100 + 200) + (300 + 400)
    assert sizes["/"] == total
    assert sizes["/subdir1/"] == (100 + 200)
    assert sizes["/subdir2/"] == (300 + 400)


def test_find_directory_size_nested_subdir_files():
    root = {
        "__name__": "/",
        "abc.txt": 100,
        "subdir1": {
            "__name__": "subdir1",
            "AAA.txt": 200,
            "subdir2": {
                "__name__": "subdir1",
                "BBB.txt": 300,
                "subdir3": {
                    "__name__": "subdir3",
                    "BBB.txt": 400,
                    "subdir4": {
                        "__name__": "subdir4",
                        "BBB.txt": 500,
                    },
                },
            },
        },
    }
    root[".."] = root
    root["subdir1"][".."] = root
    root["subdir1"]["subdir2"][".."] = root["subdir1"]
    root["subdir1"]["subdir2"]["subdir3"][".."] = root["subdir1"]["subdir2"]
    root["subdir1"]["subdir2"]["subdir3"]["subdir4"][".."] = (
        root["subdir1"]["subdir2"]["subdir3"])

    sizes = {}
    total = utils.find_directory_sizes(
        root, root["__name__"], sizes=sizes)

    assert total == (100 + 200 + 300 + 400 + 500)
    assert sizes["/"] == total
    assert sizes["/subdir1/"] == (200 + 300 + 400 + 500)
    assert sizes["/subdir1/subdir2/"] == (300 + 400 + 500)
    assert sizes["/subdir1/subdir2/subdir3/"] == (400 + 500)
    assert sizes["/subdir1/subdir2/subdir3/subdir4/"] == (500)


def test_part_1_sample_input():
    input_data = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    result = solve.part_1(input_data)
    
    assert result == 95437


def test_part_2_sample_input():
    input_data = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k",
    ]

    result = solve.part_2(input_data)
    
    assert result == 24933642
