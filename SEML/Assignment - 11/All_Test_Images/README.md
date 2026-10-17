# All Test Images & Visual Evidence Directory

**Course:** Software Engineering and Modeling Laboratory (SEML) &mdash; Assignment 11  
**Project:** [OceanCleanup2](https://github.com/adityaagurav/OceanCleanup2.git)  
**Student:** Aditya Chandrajit Deore (PRN: 124B1F116, Batch: B3)  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  

This folder contains high-resolution image evidence of all automated unit tests, IDE test explorer trees, execution metrics, and architecture diagrams for the OceanCleanup2 test suite.

## Image Catalog

| Image File | Resolution | Type | Description |
|---|---|---|---|
| `01_Maven_Test_Terminal_Build_Success.png` | 1200x780 | Terminal Screenshot | Dark mode terminal showing `mvn test` execution, 66 tests run, BUILD SUCCESS in 42.37s. |
| `02_JUnit5_Test_Runner_Tree_Explorer.png` | 1200x840 | IDE Test Explorer | VS Code / IntelliJ Test Explorer tree view showing all 66 test methods with green checkmarks. |
| `03_Test_KPI_Metrics_Dashboard.png` | 1200x700 | Quality Dashboard | SonarQube / Allure style metrics dashboard with KPI cards and breakdown table. |
| `04_BoatProgressionService_Tests_Passed.png` | 1100x680 | Component Result | 12/12 passed tests for boat tiers, speeds, capacities, and upgrade boundary checks. |
| `05_TrashCollectionService_Tests_Passed.png` | 1100x680 | Component Result | 11/11 passed tests for trash collection, weights, scoring, and `InventoryFullException`. |
| `06_EconomyAndRecyclingService_Tests_Passed.png` | 1100x680 | Component Result | 13 passed, 1 skipped test for waste-to-gold recycling, food purchases, energy drain. |
| `07_WildlifeRescueService_Tests_Passed.png` | 1100x680 | Component Result | 11/11 passed tests for projectile hit radius, rescue points, companion management. |
| `08_GameStateManagerService_Tests_Passed.png` | 1100x680 | Component Result | 7/7 passed tests for FSM lifecycle states and `InvalidGameStateException` traps. |
| `09_DayNightCycleService_Tests_Passed.png` | 1100x680 | Component Result | 11/11 passed tests for 24h celestial progression, solar noon, and 100k ticks `@Timeout`. |
| `17_OceanCleanup2_Game_Simulation.png` | 1200x675 | Simulation Render | High-resolution capture of the OceanCleanup2 3D harbor and cleanup boat. |
| `10_JUnit5_ThreeTier_Architecture.svg` | Vector SVG | Architecture Diagram | JUnit Platform, Jupiter, Vintage three-tier model diagram. |
| `11_JUnit5_Method_Lifecycle_Flow.svg` | Vector SVG | Lifecycle Flowchart | `@BeforeAll` to `@AfterAll` execution lifecycle diagram. |
| `12_OceanCleanup_Domain_Architecture.svg` | Vector SVG | Domain UML | Core entities, services, and exception architecture diagram. |
| `13_GameState_FSM_State_Diagram.svg` | Vector SVG | State Machine | GameState FSM lifecycle transitions and illegal traps. |
| `14_DayNight_Celestial_Curve_Chart.svg` | Vector SVG | Curve Chart | 24-Hour mathematical celestial curve of sun elevation & intensity. |
| `15_Test_Automation_Pipeline.svg` | Vector SVG | CI Pipeline | Maven Surefire compiler and test execution pipeline. |
| `16_Test_Execution_KPI_Dashboard.svg` | Vector SVG | KPI Card | Standalone KPI card widget. |
| `index.html` | HTML Gallery | Interactive Viewer | Visual grid gallery to browse and view all test images in Microsoft Edge. |

## How to View All Images

Open `index.html` in Microsoft Edge to browse all images in a responsive photo grid:

```powershell
Start-Process msedge.exe "c:\Users\adity\Desktop\Subjects\SEML\Assignment - 11\All_Test_Images\index.html"
```