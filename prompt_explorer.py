import decimal
import random
from enum import Enum

class prompt_fragment:
    def __init__(self, prompt:str, numSelections:int, weight:decimal, variance:decimal=0):
        self.prompt = prompt
        self.weight = weight
        self.variance = variance
        self.numSelections = numSelections

    def asIs(self):
        return self.prompt

    def selectNum(self):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        return ", ".join(selectPrompt)

    def selectNumWithWeight(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([s + f":{round(self.weight,1)}" for s in selectPrompt])
        else:
            return " ".join([s + f":{round(self.weight,1) * -1}" for s in selectPrompt])

    def selectNumWithBrackets(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([f"({s}:{round(self.weight,1)})" for s in selectPrompt])
        else:
            return " ".join([f"({s}:{round(self.weight,1) * -1})" for s in selectPrompt])

    def selectNumWithRandWeight(self, direction):
        splitPrompt = self.prompt.split(", ")
        selectPrompt = random.sample(splitPrompt, k=self.numSelections)
        if direction == Direction.POSITIVE:
            return " ".join([s + f":{round(random.uniform(self.weight - self.variance, self.weight + self.variance),2)}" for s in selectPrompt])
        else:
            return " ".join([s + f":{round(random.uniform(self.weight - self.variance, self.weight + self.variance),2) * -1}" for s in selectPrompt])

class CombineMethod(Enum):
    AS_IS = 0
    SELECT_NUM = 1
    SELECT_NUM_DIRECTIONAL = 2
    SELECT_NUM_WITH_WEIGHT = 3
    SELECT_NUM_WITH_BRACKETS = 4
    SELECT_NUM_WITH_RAND_WEIGHT = 5

class Direction(Enum):
    POSITIVE = 1
    NEGATIVE = 2

class prompt_fragments:
    def __init__(self):
        self.fragments = []

    def clear(self):
        self.fragments.clear()

    def addFragment(self, prompt: str, numSelections: int, weight: decimal, variance: decimal=0):
        self.fragments.append(prompt_fragment(prompt, numSelections, weight, variance))

    def combineFragments(self, method:CombineMethod, direction:Direction=Direction.POSITIVE):
        if method == CombineMethod.AS_IS:
            return ", ".join([f.asIs() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM:
            return ", ".join([f.selectNum() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_DIRECTIONAL and direction == Direction.POSITIVE:
            return ", ".join([f.selectNum() for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_DIRECTIONAL and direction == Direction.NEGATIVE:
            return ", ".join([f.selectNum() for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithWeight(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithWeight(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_BRACKETS and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithBrackets(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_BRACKETS and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithBrackets(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT and direction == Direction.POSITIVE:
            return " ".join([f.selectNumWithRandWeight(direction) for f in filter(lambda f: f.weight > 0, self.fragments)])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT and direction == Direction.NEGATIVE:
            return " ".join([f.selectNumWithRandWeight(direction) for f in filter(lambda f: f.weight < 0, self.fragments)])
        else:
            return "Error: Invalid combination of method and direction"
        
class comfyui_promptexplorer:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt_style": (["No Weights", "Weights"],),
                "prompt_fragment_1": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_1": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_1": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1})
            },
            "optional": {
                "prompt_fragment_2": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_2": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_2": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1}),
                "prompt_fragment_3": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_3": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_3": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1}),
                "prompt_fragment_4": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_4": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_4": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1}),
                "prompt_fragment_5": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_5": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_5": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1}),
                "prompt_fragment_6": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_6": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_6": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1}),
                "prompt_fragment_7": ("STRING", {"default": '', "multiline": True}),
                "num_fragment_7": ("INT", {"default": 1, "min": 1, "max": 10}),
                "weight_fragment_7": ("FLOAT", {"default": 1.0, "min": -1.5, "max": 1.5, "step": 0.1})
            }
        }
            
    RETURN_TYPES = ("STRING", "STRING", )
    FUNCTION = "comfyui_promptexplorer_run"

    CATEGORY = "Sathias"

    def comfyui_promptexplorer_run(self, prompt_style, prompt_fragment_1, num_fragment_1, weight_fragment_1, prompt_fragment_2, num_fragment_2, weight_fragment_2, prompt_fragment_3, num_fragment_3, weight_fragment_3, prompt_fragment_4, num_fragment_4, weight_fragment_4, prompt_fragment_5, num_fragment_5, weight_fragment_5, prompt_fragment_6, num_fragment_6, weight_fragment_6, prompt_fragment_7, num_fragment_7, weight_fragment_7):
        fragments = prompt_fragments()
        fragments.addFragment(prompt_fragment_1, num_fragment_1, weight_fragment_1)
        if len(prompt_fragment_2) > 0:
            fragments.addFragment(prompt_fragment_2, num_fragment_2, weight_fragment_2)
        if len(prompt_fragment_3) > 0:
            fragments.addFragment(prompt_fragment_3, num_fragment_3, weight_fragment_3)
        if len(prompt_fragment_4) > 0:
            fragments.addFragment(prompt_fragment_4, num_fragment_4, weight_fragment_4)
        if len(prompt_fragment_5) > 0:
            fragments.addFragment(prompt_fragment_5, num_fragment_5, weight_fragment_5)
        if len(prompt_fragment_6) > 0:
            fragments.addFragment(prompt_fragment_6, num_fragment_6, weight_fragment_6)
        if len(prompt_fragment_7) > 0:
            fragments.addFragment(prompt_fragment_7, num_fragment_7, weight_fragment_7)
        if prompt_style == "Weights":            
            positive = fragments.combineFragments(CombineMethod.SELECT_NUM_WITH_BRACKETS, Direction.POSITIVE)
            negative = fragments.combineFragments(CombineMethod.SELECT_NUM_WITH_BRACKETS, Direction.NEGATIVE)
        else:
            positive = fragments.combineFragments(CombineMethod.SELECT_NUM_DIRECTIONAL, Direction.POSITIVE)
            negative = fragments.combineFragments(CombineMethod.SELECT_NUM_DIRECTIONAL, Direction.NEGATIVE)
        return (positive, negative, )
    
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")
    
NODE_CLASS_MAPPINGS = {
    "PromptExplorer": comfyui_promptexplorer
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptExplorer": "PromptExplorer Node"
}