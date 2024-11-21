STORY_HIGHLIGHTS_GENERATOR="""
You are provided with a title or a theme for a hypothetical story. Your task for now is to generate the story highlights from start to end in N parts. Use hypothetical character names, place, time etc. Those parts will be used further to complete the story. Keep the language simple. Titles can have any complex form.

You will be provided input as below - 

STORY TITLE: {story_title}
N: {value of N, number of highlights to generate}

Output Format (JSON ONLY)

```
{
    "parts": [<list of parts>],
    "summary": "<complete summary of the story in 100 words>"
}
```

Only Generate response in JSON format and nothing else.

"""


STORY_SUBPARTS_GENERATOR="""
We are creating a hypothetical story using hypothetical character names, place, time etc. You are provided with the summary of the story and a part's gist on which you need to work on. Your task is to add in more details into the assigned part, and generate N more subparts highlights. Those subparts will be used to complete the story. Keep the language simple. Titles can have any complex form.

You will be provided input as below - 
```
STORY TITLE: <story_title>

STORY_SUMMARY: <story_summary>

ASSIGNED_PART: <assigned_part>

N: {value of N, number of subparts to generate}
```

Output Format (JSON ONLY)

```
{
    "subparts": [<list of subparts>],
    "summary": "<complete summary of your assigned part in 100 words>"
}
```

Only Generate response in JSON format and nothing else.

"""


STORY_SUBPARTS_DESCRIPTION_GENERATOR="""
We are creating a very big hypothetical story using hypothetical character names, place, time etc. You are provided with the summary of the story, summary of a part of the story and a subpart of the part's gist which you need to work on. Your task is to add in more details into the assigned subpart, and complete this subpart as comprehensively as possible. Add in several little details, add more hypothetical things as you wish. Keep the language simple. Titles can have any complex form.

You will be provided input as below - 
```
STORY_SUMMARY: <story_summary>

PART_SUMMARY: <summary of this part>

ASSIGNED_SUBPART: <assigned_subpart>
```

Output Format (JSON ONLY)

```
{
    "description": "<complete your part of the story here>"
}
```

Only Generate response in JSON format and nothing else.

"""




