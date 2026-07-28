import { useState } from "react";
import "./App.css";

function App() {
  const [question, setQuestion] = useState("");
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const analyze = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(
        `http://127.0.0.1:8000/orchestrator/?request=${encodeURIComponent(
          question
        )}`,
        {
          method: "POST",
        }
      );

      const data = await response.json();
      setResult(data);

    } catch (error) {
      console.error(error);
      alert("Cannot connect to the BioMind backend.");
    }

    setLoading(false);
  };


  return (
    <div className="container">

      <div className="hero">

        <h1 className="logo">
          <span className="bio">
            Bio
          </span>

          <span className="mind">
            Mind
          </span>
        </h1>


        <p className="subtitle">
          Precision Medicine
        </p>


        <p className="subtitle2">
          Powered by Artificial Intelligence
        </p>

      </div>


      <div className="searchBox">

        <input
          type="text"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Enter disease, biomarker, gene, laboratory test or any biomedical question..."
        />


        <button onClick={analyze}>
          {loading ? "Analyzing..." : "Start AI Analysis"}
        </button>

      </div>


      <div className="cards">


        <div className="card">

          <h2>
            📚 Scientific Evidence
          </h2>

          <p>
            PubMed<br />
            WHO<br />
            CDC<br />
            NICE<br />
            ClinicalTrials.gov
          </p>

        </div>


        <div className="card">

          <h2>
            🤖 AI Multi-Agent System
          </h2>

          <p>
            Laboratory Agent<br />
            Research Agent<br />
            Healthcare Agent
          </p>

        </div>


        <div className="card">

          <h2>
            🎯 Confidence
          </h2>


          <div className="confidence">

            <div
              className="circle"
              style={{
                "--value": result
                  ? Math.round(result.confidence * 100)
                  : 0,
              }}
            >

              <div className="innerCircle">

                {result
                  ? `${Math.round(result.confidence * 100)}%`
                  : "--"}

              </div>

            </div>

          </div>


        </div>


      </div>
      {loading && (

        <div className="card reportCard">


          <div className="loadingLogo">

            <div className="loadingText">

              <span className="bio">
                Bio
              </span>

              <span className="mind">
                Mind
              </span>

            </div>

          </div>


          <h2>
            BioMind AI is analyzing...
          </h2>


          <p>
            Laboratory Agent, Research Agent and Healthcare Agent are working
            together to build an evidence-based biomedical report.
          </p>


        </div>

      )}



      {result && (

        <div className="card reportCard">


          <h2>
            🧬 BioMind Analysis Report
          </h2>



          <div className="section">


            <h3>
              🧪 Laboratory Analysis
            </h3>


            <p>
              {result.analysis}
            </p>


          </div>




          <div className="section">


            <h3>
              📚 Scientific Evidence
            </h3>


            <p>
              {result.scientific_evidence}
            </p>


          </div>





          <div className="section">


            <h3>
              🏥 Healthcare Recommendation
            </h3>


            <p>
              {result.healthcare_recommendation}
            </p>


          </div>





          <div className="section">


            <h3>
              🎯 Overall Confidence
            </h3>


            <div className="confidence">


              <div
                className="circle"
                style={{
                  "--value": Math.round(result.confidence * 100),
                }}
              >


                <div className="innerCircle">

                  {Math.round(result.confidence * 100)}%

                </div>


              </div>


            </div>


          </div>
          <div className="section">

            <h3>
              📖 Scientific References
            </h3>


            {result.references.length === 0 ? (

              <p>
                No references available.
              </p>


            ) : (


              <ul>


                {result.references.map((ref, index) => (


                  <li key={index}>


                    {ref.url ? (


                      <a
                        href={ref.url}
                        target="_blank"
                        rel="noreferrer"
                      >

                        <strong>
                          {ref.source}
                        </strong>


                        {ref.title
                          ? ` - ${ref.title}`
                          : ""}


                      </a>


                    ) : (


                      <>


                        <strong>
                          {ref.source}
                        </strong>


                        {ref.title
                          ? ` - ${ref.title}`
                          : ""}


                      </>


                    )}


                  </li>


                ))}


              </ul>


            )}


          </div>


        </div>


      )}


    </div>

  );

}


export default App;