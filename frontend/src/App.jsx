import { useState } from "react";
import ChatPanel from "./components/ChatPanel";
import MissionUnderstanding from "./components/MissionUnderstanding";
import Recommendation from "./components/Recommendation";
import CandidatePlans from "./components/CandidatePlans";
import EvidenceSection from "./components/EvidenceSection";
import RejectedAlternatives from "./components/RejectedAlternatives";
import Explanation from "./components/Explanation";
import MarineMap from "./components/MarineMap";
import "./styles.css";

function App() {
  const [conversationHistory, setConversationHistory] = useState([]);
  const [data, setData] = useState(null);
  const [status, setStatus] = useState("Ready for mission input.");
  const [loading, setLoading] = useState(false);

  const analyzeMission = async (mission) => {
    if (!mission.trim()) {
      setStatus("Please enter a marine mission.");
      return;
    }

    const userMessage = {
      role: "user",
      content: mission.trim(),
    };

    const updatedHistory = [...conversationHistory, userMessage];

    setConversationHistory(updatedHistory);
    setStatus("ORCA is analyzing your mission...");
    setLoading(true);

    try {
      const response = await fetch("/api/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          mission: mission.trim(),
          conversation_history: updatedHistory,
        }),
      });

      const result = await response.json();

      if (!response.ok) {
        throw new Error(result.error || "Mission analysis failed.");
      }

      setData(result);

      const orcaMessage = {
        role: "assistant",
        content: result.ai_explanation,
      };

      setConversationHistory((previous) => [
        ...previous,
        orcaMessage,
      ]);

      setStatus("Mission analyzed successfully.");
    } catch (error) {
      console.error(error);
      setStatus(`Error: ${error.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <header className="header">
        <h1>ORCA</h1>
        <p>Marine Intelligence &amp; Decision Support</p>
      </header>

      <main className="container">

        <ChatPanel
          conversationHistory={conversationHistory}
          onAnalyze={analyzeMission}
          status={status}
          loading={loading}
        />

        {data && (
          <>
            <MissionUnderstanding mission={data.mission} />

            <Recommendation
              recommendation={data.recommendation}
            />

            <EvidenceSection
              evidence={data.recommendation.evidence}
            />

            <CandidatePlans
              plans={data.plans}
              recommendation={data.recommendation}
            />

            <RejectedAlternatives
              rejectedPlans={data.recommendation.rejected_plans}
            />

            <Explanation
              explanation={data.ai_explanation}
            />
          </>
        )}

        <MarineMap data={data} />

      </main>
    </>
  );
}

export default App;