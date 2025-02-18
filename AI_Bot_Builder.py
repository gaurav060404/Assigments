class UnknownCommandError(Exception):
    pass

class SelfDestructionError(Exception):
    pass

def execute_commands(commands):
    for command in commands:
        try:
            if command == "explode":
                raise SelfDestructionError("ERROR: Jeeves cannot self-destruct!")
            elif command not in ["clean", "cook", "dance"]:
                raise UnknownCommandError(f"ERROR: Unknown command '{command}'")
            else:
                print(f"Executing {command}...")
        except (UnknownCommandError, SelfDestructionError) as e:
            print(e)

commands_list = ["clean", "cook", "dance", "explode", "fly"]
execute_commands(commands_list)
