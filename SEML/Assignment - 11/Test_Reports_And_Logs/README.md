# OceanCleanup2 &mdash; Automated JUnit 5 Test Reports and Runtime Logs

**Course:** Software Engineering and Modeling Laboratory (SEML) &mdash; Assignment 11  
**Institution:** Pimpri Chinchwad College of Engineering (PCCOE), Pune  
**Student Name:** Aditya Chandrajit Deore  
**PRN:** 124B1F116 | **Batch:** B3  
**Project Tested:** [OceanCleanup2 (GitHub Repository)](https://github.com/adityaagurav/OceanCleanup2.git)  
**Execution Date:** 17th October 2026  
**Build Engine:** Apache Maven 3.9.16 | **JVM:** OpenJDK 21 LTS (Temurin-21.0.12+8)

---

## 1. Overview and Scope

This directory contains the complete set of automated execution logs, Surefire XML reports, test console outputs, and verification metrics for the **OceanCleanup2** testing suite. The tests verify the correctness, mathematical integrity, boundary handling, and deterministic exception throwing of the core domain logic:

1. **Boat Progression & Capacity Tiers:** Levels 1 to 4 (Slots: 20–120, Speed: 12–20 knots), upgrade thresholds, boundary limits.
2. **Litter Harvesting & Physics:** GPU-instanced trash collection, proximity reel detection, score tabulation, and `InventoryFullException`.
3. **Recycling Economy & Bio-Restoration:** Waste-to-gold recycling conversions, food purchases, sleep restoration, and `InsufficientFundsException`.
4. **Wildlife Sanctuary & Companion Physics:** Marine rescue hitbox collision physics (\(r = 	ext{scale} \times 4.0\)), companion bonding, and companion swap integrity.
5. **Finite State Machine Lifecycle:** State transitions (`LOADING`, `PLAYING`, `PAUSED`, `GAMEOVER`) and `InvalidGameStateException` traps.
6. **24-Hour Celestial Simulation:** Sinusoidal solar elevation curves, solar intensity calculation, day counter rollover, and performance timeout testing (100,000 ticks < 1s).

---

## 2. Directory Manifest & Log Files

| File Name | Format | Description |
|---|---|---|
| `01_Full_Maven_Build_And_Test.log` | Text Log | Raw console output from `mvn clean test` showing compiler and Surefire plugin outputs. |
| `02_TestSuite_Execution_Summary.log` | Text Log | High-level summary of test results, metrics table, and quality assurance sign-offs. |
| `03_BoatProgressionService_Detailed_Log.log` | Text Log | Detailed execution trace for all 12 tests in `BoatProgressionServiceTest`. |
| `04_TrashCollectionService_Detailed_Log.log` | Text Log | Detailed execution trace for all 11 tests in `TrashCollectionServiceTest`. |
| `05_EconomyAndRecyclingService_Detailed_Log.log` | Text Log | Detailed execution trace for all 14 tests in `EconomyAndRecyclingServiceTest`. |
| `06_WildlifeRescueService_Detailed_Log.log` | Text Log | Detailed execution trace for all 11 tests in `WildlifeRescueServiceTest`. |
| `07_GameStateManagerService_Detailed_Log.log` | Text Log | Detailed execution trace for all 7 tests in `GameStateManagerServiceTest`. |
| `08_DayNightCycleService_Detailed_Log.log` | Text Log | Detailed execution trace for all 11 tests in `DayNightCycleServiceTest`. |
| `TEST-com.oceancleanup.*.xml` | JUnit XML | Standardized JUnit 5 XML reports (7 files) for CI/CD ingestion (Jenkins, GitHub Actions). |
| `com.oceancleanup.*.txt` | Surefire TXT | Surefire execution reports for each individual test class. |

---

## 3. Test Suite Metrics & Results Summary

```
------------------------------------------------------------------------------------------------------------------------
Test Suite Class Name                      Total Tests   Passed   Failed   Errors   Skipped   Pass Rate   Execution Time
------------------------------------------------------------------------------------------------------------------------
BoatProgressionServiceTest                     12          12        0        0        0       100.0%         0.132s
TrashCollectionServiceTest                     11          11        0        0        0       100.0%         0.264s
EconomyAndRecyclingServiceTest                 14          13        0        0        1       100.0%*        0.256s
WildlifeRescueServiceTest                      11          11        0        0        0       100.0%         0.348s
GameStateManagerServiceTest                     7           7        0        0        0       100.0%         0.144s
DayNightCycleServiceTest                       11          11        0        0        0       100.0%         0.552s
------------------------------------------------------------------------------------------------------------------------
Cumulative Total Metrics                       66          65        0        0        1       100.0%         1.696s (Test)
                                                                                                             42.376s (Build)
------------------------------------------------------------------------------------------------------------------------
```
*\*Note: 1 test in `EconomyAndRecyclingServiceTest` (`testBankLoanFacility`) is marked `@Disabled` as documented for the future v3.0 micro-finance roadmap. Active pass rate is 100.0% (65/65 active tests passed).*

---

## 4. How to Reproduce and Re-run the Tests

Ensure Java 21 and Maven are installed and available in your terminal:

```bash
# 1. Navigate to the Java test project directory
cd "c:\Users\adity\Desktop\Subjects\SEML\Assignment - 11\OceanCleanup-JUnit5-Testing"

# 2. Run the complete automated test suite
mvn clean test

# 3. View individual Surefire XML reports
dir target\surefire-reports
```

---

## 5. Summary of Key Quality Findings

- **Zero Regressions:** 100% of functional requirements pass cleanly across all six domain services.
- **Boundary Precision:** BVA confirmed that boats strictly prohibit upgrades beyond Level 4 and refuse upgrades when trash counts are even 1 below threshold.
- **Exception Containment:** Critical edge scenarios (`InventoryFullException`, `InsufficientFundsException`, `InvalidGameStateException`) are reliably caught and handled.
- **Performance:** Day/Night cycle simulation passed 100,000 tick updates in under 50ms, well below the 800ms preemptive timeout limit.