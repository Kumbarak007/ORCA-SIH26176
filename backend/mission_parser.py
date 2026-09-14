import json

from llm_client import LLMClient


class MissionParser:
    """
    ORCA Mission Parser.

    Uses the LLM to convert a natural-language mission
    into structured mission information.
    """

    def __init__(self):
        self.name = "Mission Parser"
        self.llm = LLMClient()

    def parse_mission(self, user_input, conversation_history=None):
        if conversation_history is None:
            conversation_history = []

        conversation_context = "\n".join(
            [
                f"{item.get('role', 'user')}:"
                f"{item.get('content', '')}"
                for item in conversation_history
            ]
        )    
        """
        Convert a natural-language mission into structured JSON.
        """

        prompt = f"""
You are the Mission Parser for ORCA, a marine mission
decision intelligence system.

Convert the user's natural-language mission into JSON.

Extract only the following fields:

{{
    "is_marine_mission": true,
    "objective": "",
    "location": "",
    "departure_time": "",
    "fishing_duration_hours": null,
    "return_deadline": "",
    "avoid_high_wind": true,
    "avoid_unsafe_sea": true,
    "avoid_restricted_areas": true,
    "max_wave_height": null,
    "maximize_fishing_potential": true,
    "minimize_risk": true,
    "minimize_travel_distance": true
    "primary_preference": ""
}}

Rules:

Determine whether the user's latest message is actually a marine mission request or a follow-up that modifies an existing marine mission.

Set is_marine_mission to true when:
- The user is requesting a marine/fishing mission.
- The user is providing or modifying mission constraints, preferences, timing, location, safety requirements, or other details related to an existing marine mission.

Set is_marine_mission to false when:
- The message is casual conversation.
- The message is unrelated to marine mission planning.
- The user is greeting the assistant without providing a mission.
- The message cannot reasonably be interpreted as a marine mission or mission follow-up.

Do not invent a marine mission from an unrelated message.

1. Return ONLY valid JSON.
2. Do not add markdown or explanations.
3. Do not invent information that the user did not provide.
4. If a value is unknown, use an empty string or null.
5. Keep the user's intended objective.
6. Keep safety preferences explicit.
7. If the current message modifies or asks about the previous
   mission, preserve the previous mission information and
   apply the new requirement.
8. Treat follow-up messages such as "what if...", "change...",
   "instead...", "also avoid...", or "make it..." as updates
   to the existing mission when appropriate.
9. Return the complete updated mission, not only the changed field.
10. If the user specifies a maximum wave height, extract it
    as max_wave_height in meters.
11. If no maximum wave height is specified, return null.
12. For phrases such as "waves below 1 meter", "wave height
    under 1 m", or "keep waves below 0.8 meters", extract
    the numerical value in meters.
19. Identify the user's primary preference and return it as
    primary_preference.

20. If the user prioritizes fishing potential, highest fishing
    potential, maximum fishing opportunity, or best fishing,
    set primary_preference to "fishing_potential".

21. If the user prioritizes safety, minimum risk, calm weather,
    safe conditions, or the safest zone, set primary_preference
    to "safety".

22. If the user prioritizes shortest travel, closest zone,
    minimum distance, or least travel, set primary_preference
    to "distance".

23.  If no clear primary preference is stated, set
    primary_preference to "balanced".

24. When a follow-up changes the user's priority, update
    primary_preference accordingly while preserving the rest
    of the mission.

25. Do not always return "balanced". Carefully inspect the
    current user message and conversation history for explicit
    priority words such as "prioritize", "highest", "best",
    "safest", "closest", "minimum distance", or similar terms.


Conversation history:
{conversation_context}

Current user message:
{user_input}
"""

        response = self.llm.generate(prompt).strip()

        try:
            parsed_data = json.loads(response)

        except json.JSONDecodeError:

            cleaned_response = response

            if cleaned_response.startswith("'''"):
                cleaned_response = cleaned_response.replace(
                    "```json", ""
                ).replace(
                    "'''", ""
                ).strip()

            try:
                parsed_data = json.loads(cleaned_response)

            except json.JSONDecodeError:

                # Try extracting the JSON object from surrounding text
                start = cleaned_response.find("{")
                end = cleaned_response.rfind("}")

                if start != -1 and end != -1:
                    json_text = cleaned_response[start:end + 1]

                    try:
                        parsed_data = json.loads(json_text)

                    except json.JSONDecodeError:
                        raise ValueError(
                            "Gemini returned an invalid mission JSON."
                        )

                else:
                    raise ValueError(
                        "Gemini returned an invalid mission JSON."
                    )                

        # ORCA safety constraints are enabled by default.
        # The LLM must not disable them accidentally.
        parsed_data["avoid_high_wind"] = True
        parsed_data["avoid_unsafe_sea"] = True
        parsed_data["avoid_restricted_areas"] = True

        return parsed_data