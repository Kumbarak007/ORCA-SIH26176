import { useState, useEffect, useRef } from "react";

function ChatPanel({
  conversationHistory,
  onAnalyze,
  status,
  loading,
}) {
  const [input, setInput] = useState("");
  const chatWindowRef = useRef(null);

  useEffect(() => {
    if (chatWindowRef.current) {
      chatWindowRef.current.scrollTop =
        chatWindowRef.current.scrollHeight;
    }
  }, [conversationHistory, loading]);

  const handleSubmit = () => {
    const mission = input.trim();

    if (!mission || loading) {
      return;
    }

    onAnalyze(mission);
    setInput("");
  };

  const handleKeyDown = (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      handleSubmit();
    }
  };

  return (
    <div className="card">

      <h2>ORCA Marine Mission Assistant</h2>

      <p>
        Describe your marine mission naturally.
        ORCA will analyze your request using marine,
        weather, PFZ and GIS evidence.
      </p>

      <div
        id="chatWindow"
        className="chat-window"
        ref={chatWindowRef}
      >

        {conversationHistory.length === 0 && (
          <div className="chat-message orca-message">
            <div className="chat-label">ORCA</div>

            <div className="chat-bubble">
              Hello! Describe the marine mission you want
              to plan. You can also modify the mission after
              I analyze it.
            </div>
          </div>
        )}

        {conversationHistory.map((message, index) => (
          <div
            key={index}
            className={`chat-message ${
              message.role === "user"
                ? "user-message"
                : "orca-message"
            }`}
          >
            <div className="chat-label">
              {message.role === "user" ? "YOU" : "ORCA"}
            </div>

            <div className="chat-bubble">
              {message.content}
            </div>
          </div>
        ))}

        {loading && (
          <div className="chat-message orca-message">
            <div className="chat-label">ORCA</div>

            <div className="chat-bubble">
              ORCA is analyzing your mission...
            </div>
          </div>
        )}

      </div>

      <div className="chat-input-area">

        <textarea
          id="missionInput"
          value={input}
          onChange={(event) => setInput(event.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Example: I want to go fishing near Goa tomorrow morning for 5 hours. Avoid high wind and restricted areas."
          disabled={loading}
        />

        <button
          type="button"
          onClick={handleSubmit}
          disabled={loading}
        >
          {loading ? "Analyzing..." : "Send Mission"}
        </button>

      </div>

      <div className="status">
        {status}
      </div>

    </div>
  );
}

export default ChatPanel;