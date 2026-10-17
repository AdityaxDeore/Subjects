package com.oceancleanup;

import org.junit.platform.suite.api.SelectClasses;
import org.junit.platform.suite.api.Suite;
import org.junit.platform.suite.api.SuiteDisplayName;

/**
 * Master Test Suite bundling all individual component test classes for OceanCleanup.
 */
@Suite
@SuiteDisplayName("OceanCleanup Complete Automated Test Suite")
@SelectClasses({
        BoatProgressionServiceTest.class,
        TrashCollectionServiceTest.class,
        EconomyAndRecyclingServiceTest.class,
        WildlifeRescueServiceTest.class,
        GameStateManagerServiceTest.class,
        DayNightCycleServiceTest.class
})
public class OceanCleanupTestSuite {
    // JUnit Platform Suite placeholder class
}
