import json
from enum import Enum


def process_input(move_to_next_line):
    user_input = input()
    if user_input == "stats":
        for key, value in Player.items():
            number_of_tabs = int((15 - len(key)) / 4)
            tabs = "\t" * number_of_tabs
            print(f"{key}{tabs}: {value}")
        return process_input(move_to_next_line)
    elif not move_to_next_line:
        return user_input


Player = {
    "Name": "No Name",
    "Health": 10,
    "Strength": 10,
    "Agility": 10,
    "Mana": 10
}


class GameState(Enum):
    MENU = 0
    IN_GAME = 1
    END = 2


class Story:
    currentStorySegment = "intro"
    currentStorySegmentPos = 0
    linesOfTheStory = json.load(open("story.json"))
    game_state = GameState(GameState.IN_GAME)

    @staticmethod
    def get_specific_line(story_segment, segment_pos):
        return Story.linesOfTheStory[story_segment][segment_pos]["text"]

    @staticmethod
    def current_line_needs_input():
        return Story.linesOfTheStory[Story.currentStorySegment][Story.currentStorySegmentPos]["input_required"]

    @staticmethod
    def progress_story():
        current_line_info = Story.linesOfTheStory[Story.currentStorySegment][Story.currentStorySegmentPos]
        print(current_line_info["text"].replace("{player_name}", Player["Name"]))

        if "input_required" in current_line_info:
            loop_until_correct_result = False
            if "possible_inputs" in current_line_info:
                loop_until_correct_result = True

            while True:
                user_input = process_input(False)

                if "possible_inputs" in current_line_info:
                    for possible_options in current_line_info["possible_inputs"]:
                        if user_input == possible_options:
                            loop_until_correct_result = False
                            break

                if not loop_until_correct_result:
                    break
                else:
                    print("That is not a valid option, try again:")

            if "input_change_var" in current_line_info and current_line_info["input_change_var"] == "player_name":
                Player["Name"] = user_input
            elif "input_new_story_pos" in current_line_info:
                Story.currentStorySegment = current_line_info["input_new_story_pos"][user_input][0]
                Story.currentStorySegmentPos = current_line_info["input_new_story_pos"][user_input][1]
                return

        # no user input required here
        if "change_state" in current_line_info:
            new_state = current_line_info["change_state"]
            if new_state == "END":
                Story.game_state = GameState.END
            elif new_state == "IN_GAME":
                Story.game_state = GameState.IN_GAME
            elif new_state == "MENU":
                Story.game_state = GameState.MENU

        if not Story.game_state == GameState.END:
            Story.currentStorySegmentPos += 1
            if "input_required" not in current_line_info:
                process_input(True)


if __name__ == '__main__':
    # menu stuff
    Story.game_state = GameState.IN_GAME

    while Story.game_state is GameState.IN_GAME:
        Story.progress_story()
