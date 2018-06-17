function Objective() {
  return (
    <div>
      <h2> OBJECTIVE </h2>
      <p>Committed and highly motivated engineer seeking to deepen my knowledge of Machine Learning techniques and applications through the pursuit of higher education.</p>
    </div>
  );
}
function Skills() {
  return (
    <div>
      <h2> SKILLS </h2>
        <p>Languages:  JavaScript, Python (Keras, Tensorflow, scikit-learn, Pandas, NumPy, MySQL, matplotlib), HTML, CSS, SQL, C++, Java</p>
        <p>Frameworks/Libraries:  jQuery, Knockout.js (MVVM), ReactJS, Flask, ROS</p>
        <p>Other:  Git/GitHub, MIPs, Transfer Learning</p>
    </div>
  );
}
function Projects() {
  return (
    <div>
      <h2> PROJECTS </h2>
      <h4> Deep Q-Learning Virtual  Quadcopter  - <a className="cv_links" href="https://github.com/JPatrick9793/RL-Quadcopter">Github</a><span className="cv_dates"> (March 2018)</span></h4>
      <ul>
        <li>Taught a virtual Quadcopter different flight patterns using Deep-Q Reinforcement learning.</li>
        <li>Utilizes actor-critic methods using python and keras. Udacity provided the Unity engine and ROS environment.
</li>
      </ul>
      <h4> CNN Dog Breed Classifier  - <a className="cv_links" href="https://github.com/JPatrick9793/dog-project ">Github</a><span className="cv_dates"> (November 2017)</span></h4>
      <ul>
        <li>Developed an algorithm to identify 133 varieties of canine breed given an image of a dog or human.</li>
        <li>Implements a Convolutional Neural Network trained on 8351 dog images and 13233 human images.
</li>
        <li>Transfer learning from ResNet50 model. Achieved over 80% testing accuracy.</li>
      </ul>
      <h4> Sudoku Solver - <a className="cv_links" href="http://www.TheJohnConway.com/Projects/Sudoku_Solver">Link</a><span className="cv_dates"> (March 2018)</span></h4>
      <ul>
        <li>Application to solve Sudoku Puzzles by treating them as a constraint satisfaction problem.</li>
        <li>Created using AC3 and backtracking search Algorithms.
</li>
      </ul>
      <h4> CRUD Catalog Website - <a className="cv_links" href="http://18.216.143.250.nip.io/catalog">Link</a><span className="cv_dates"> (December 2017)</span></h4>
      <ul>
        <li>Created a Catalog App allowing CRUD (Create, Read, Update, Destroy) operations on a server-side database.</li>
        <li>Utilizes Google OAuth 2.0, MySQL, Python, and Flask.
</li>
      </ul>
      <h4> Neighborhood Map - <a className="cv_links" href="http://www.thejohnconway.com/Projects/GoogleMap">Link</a><span className="cv_dates"> (October 2017)</span></h4>
      <ul>
        <li>Developed a custom webpage to easily search for nearby restaurants and see their hours, ratings, and geographic location.</li>
        <li>Incorporates Google Maps API, Foursquare APE, Javascript and Knockout Framework.
</li>
      </ul>
    </div>
  );
}
function Experience() {
  return (
    <div>
      <h2>Professional Experience</h2>
      <h4>S&S Fire Suppression Systems - Project Manager<span className="cv_dates"> (September 2016 - Present)</span></h4>
      <ul>
        <li>Collaborated with senior management and department heads to create the service project manager position.</li>
        <li>Managed more than 100 service contract projects from sale to completion, generating over $500,000 revenue annually.</li>
        <li>Coordinated between designers, contractors, and technicians to ensure quality service and timely completion of projects.</li>
      </ul>
      
      <h4>S&S Fire Suppression Systems - Design Engineer<span className="cv_dates"> (November 2015 - September 2016)</span></h4>
      <ul>
        <li>Developed models for fire protection system designs for optimized hydraulic performance and efficient installation costs.</li>
        <li>Worked in multifunctional and diverse teams consisting of engineers, estimators, technicians, and suppliers.</li>
      </ul>
      
      <h4>NYS Pool Management - Lifeguard Manager <span className="cv_dates"> (May 2015 - October 2016)</span></h4>
      <ul>
        <li>Managed more than 40 lifeguards at over 30 different locations across New York and New Jersey.</li>
        <li>Maintained effective and professional communication between lifeguards and upper management.</li>
      </ul>
      
      <h4>TransCanada - Compliance Intern (Ravenswood Powerplant) <span className="cv_dates"> (May 2014 - September 2014)</span></h4>
      <ul>
        <li>Identified safety-related issues throughout the plant during regular site inspections.</li>
        <li>Purchased safety equipment, created work orders, and tracked issues until completion.</li>
        <li>Shadowed various departments undergoing specialized projects including IT, Operations, and Maintenance.</li>
        <li>Worked on several different safety-related projects while simultaneously ensuring deadlines were achieved and protocols adhered to.</li>
      </ul>
    </div>
  );
}
function Education() {
  return (
    <div>
      <h2> EDUCATION </h2>
      <h4>
        ColumbiaX Artificial Intelligence MicroMasters
        <span className="cv_dates"> (January 2018 - May 2018)</span>
      </h4>
      <h4>
        Udacity Deep Learning Nanodegree
        <span className="cv_dates"> (December 2017 - March 2018)</span>
      </h4>
      <h4>
        Udacity Fullstack Web Developer Nanodegree
        <span className="cv_dates"> (September 2017 - January 2018)</span>
      </h4>
      <h4>
        Bachelor of Science, Industrial Engineering
        <span className="cv_dates"> (September 2011 - September 2015)</span>
      </h4>
      <ul>
        <li>University of Massachusetts, Amherst</li>
        <li>Engineering Management Minor</li>
      </ul>
    </div>
  );
}
function Selected_Coursework() {
  return (
    <div>
      <h2> SELECTED COURSEWORK </h2>
      <p>Machine Learning, Artificial Intelligence, Animation and CGI Motion, Robotics, Data Structures (C++), Computer Architecture (MIPs), Multivariable Calculus, Differential Equations, Linear Algebra, Design of Experiments (ANOVA)</p>
    </div>
  );
}
function Certifications() {
  return (
    <div>
      <h2>HONORS & CERTIFICATIONS</h2>
      <ul>
        <li>Engineer in Training (E.I.T.) - New York State (#093489) <span className="cv_dates">(March 2018)</span></li>
        <li>National Society of Collegiate Scholars <span className="cv_dates">(September 2011 - May 2015)</span></li>
        <li>Division 1 athlete - Men’s Swimming <span className="cv_dates">(September 2011 - May 2015)</span></li>
      </ul>
    </div>
  );
}

class CV extends React.Component {
  render() {
    return (
      <div>
        <Objective />
        <Skills />
        <Projects />
        <Experience />
        <Education />
        <Selected_Coursework />
        <Certifications />
      </div>
    );
  }
}

ReactDOM.render(
  <CV />,
  document.getElementById("app")
);
