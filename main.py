def process_input():
    return input()


class Story:
    currentStorySegment = 0
    currentStorySegmentPos = 0

    @staticmethod
    def get_specific_line(story_segment, segment_pos):
        return Story.linesOfTheStory[story_segment][segment_pos]

    linesOfTheStory = [["Once upon a time there was a...",
                        "And this one was a..."],
                       ["Welcome to story segment 2..."]]


if __name__ == '__main__':
    print(Story.get_specific_line(0, 0))
    print(Story.get_specific_line(0, 1))
    print(Story.get_specific_line(1, 0))
