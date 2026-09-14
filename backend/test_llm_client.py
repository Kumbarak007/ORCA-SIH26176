from llm_client import LLMClient


client = LLMClient()

response = client.generate(
    "You are ORCA, a marine mission planning assistant. "
    "Reply with exactly: ORCA LLM connection successful."
)

print("\n===== ORCA LLM CLIENT TEST =====\n")
print(response)
print("\n===== TEST PASSED =====")