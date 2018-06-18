var projectLinks = {
  'eightPuzzle': '/Projects/Eight_Puzzle_Solver',
  'sudokuSolver': '/Projects/Sudoku_Solver',
  'catalogWebsite': 'http://18.216.143.250.nip.io/catalog',
  'neighborhoodMap': '/Projects/GoogleMap'
};
function EightPuzzle() {
  return (
    <div className="project_bubble">
        <a 
          href={projectLinks.eightPuzzle} 
          className="project_link"
          >
          EIGHT PUZZLE SOLVER</a>
    </div>
  );
}
function SudokuSolver() {
  return (
    <div className="project_bubble">
      <a
        href={projectLinks.sudokuSolver} 
        className="project_link"
        >
        SUDOKU SOLVER</a>
    </div>
  );
}
function CatalogWebsite() {
  return (
    <div className="project_bubble">
      <a
        href={projectLinks.catalogWebsite} 
        className="project_link"
        >
        CATALOG WEBSITE</a>
    </div>
  );
}
function NeighborhoodMap() {
  return (
    <div className="project_bubble">
      <a
        href={projectLinks.neighborhoodMap} 
        className="project_link"
        >
        NEIGHBORHOOD MAP</a>
    </div>
  );
}

class Projects extends React.Component {
  render() {
    return (
      <div className="projectsMain">
        <EightPuzzle />
        <SudokuSolver />
        <CatalogWebsite />
        <NeighborhoodMap />
      </div>
    );
  }
}

ReactDOM.render(
  <Projects />,
  document.getElementById("app")
);
