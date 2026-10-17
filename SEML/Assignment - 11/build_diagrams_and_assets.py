import os
import shutil

output_dir = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 11"
os.makedirs(output_dir, exist_ok=True)

# Copy the game screenshot from OceanCleanup2
src_game_bg = os.path.join(output_dir, "OceanCleanup2", "public", "background", "harbor-background.png")
dst_game_bg = os.path.join(output_dir, "oceancleanup_game_preview.png")
if os.path.exists(src_game_bg):
    shutil.copyfile(src_game_bg, dst_game_bg)
    print("Copied harbor-background.png to oceancleanup_game_preview.png")

# -------------------------------------------------------------------------------------------------
# DIAGRAM 1: JUnit 5 Three-Tier Architecture
# -------------------------------------------------------------------------------------------------
diagram_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 380" width="100%" height="380" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow1" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <linearGradient id="grad_client" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3b82f6"/>
      <stop offset="100%" stop-color="#1d4ed8"/>
    </linearGradient>
    <linearGradient id="grad_platform" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#0284c7"/>
    </linearGradient>
    <linearGradient id="grad_jupiter" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#ecfdf5"/>
      <stop offset="100%" stop-color="#d1fae5"/>
    </linearGradient>
    <linearGradient id="grad_vintage" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fffbeb"/>
      <stop offset="100%" stop-color="#fef3c7"/>
    </linearGradient>
    <linearGradient id="grad_third" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#f5f3ff"/>
      <stop offset="100%" stop-color="#ede9fe"/>
    </linearGradient>
    <marker id="arr1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#475569"/>
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="15" width="820" height="38" rx="6" fill="#0f172a"/>
  <text x="430" y="39" font-size="14" font-weight="bold" fill="#ffffff" text-anchor="middle" letter-spacing="0.5">
    JUNIT 5 MODULAR THREE-TIER ARCHITECTURE
  </text>

  <!-- TIER 1: Client Layer (IDEs & Build Tools) -->
  <g transform="translate(40, 70)">
    <rect x="0" y="0" width="780" height="56" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow1)"/>
    <text x="20" y="24" font-size="11" font-weight="bold" fill="#64748b" text-transform="uppercase">Client Tier: IDEs &amp; Build Systems</text>
    
    <!-- Pills -->
    <rect x="190" y="12" width="100" height="32" rx="6" fill="url(#grad_client)"/>
    <text x="240" y="33" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Maven (Surefire)</text>

    <rect x="305" y="12" width="85" height="32" rx="6" fill="url(#grad_client)"/>
    <text x="347" y="33" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Gradle</text>

    <rect x="405" y="12" width="105" height="32" rx="6" fill="url(#grad_client)"/>
    <text x="457" y="33" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">IntelliJ IDEA</text>

    <rect x="525" y="12" width="85" height="32" rx="6" fill="url(#grad_client)"/>
    <text x="567" y="33" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">Eclipse</text>

    <rect x="625" y="12" width="135" height="32" rx="6" fill="url(#grad_client)"/>
    <text x="692" y="33" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">VS Code / Console</text>
  </g>

  <!-- Flow Arrows 1 -->
  <line x1="430" y1="128" x2="430" y2="152" stroke="#475569" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- TIER 2: JUnit Platform -->
  <g transform="translate(40, 155)">
    <rect x="0" y="0" width="780" height="65" rx="8" fill="url(#grad_platform)" filter="url(#shadow1)"/>
    <text x="390" y="26" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">
      JUnit Platform (org.junit.platform)
    </text>
    <text x="390" y="47" font-size="11" fill="#e0f2fe" text-anchor="middle">
      TestEngine API &bull; Launcher &bull; Discovery Engine &bull; Console Runner &bull; Suite Aggregation (@Suite)
    </text>
  </g>

  <!-- Flow Arrows 2 (Branching to 3 engines) -->
  <line x1="200" y1="222" x2="200" y2="252" stroke="#475569" stroke-width="2.2" marker-end="url(#arr1)"/>
  <line x1="430" y1="222" x2="430" y2="252" stroke="#475569" stroke-width="2.2" marker-end="url(#arr1)"/>
  <line x1="660" y1="222" x2="660" y2="252" stroke="#475569" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- TIER 3: Engines -->
  <!-- 3A: Jupiter Engine -->
  <g transform="translate(40, 255)">
    <rect x="0" y="0" width="310" height="105" rx="8" fill="url(#grad_jupiter)" stroke="#059669" stroke-width="1.8" filter="url(#shadow1)"/>
    <rect x="12" y="10" width="110" height="20" rx="4" fill="#059669"/>
    <text x="67" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">PRIMARY ENGINE</text>
    <text x="130" y="25" font-size="12" font-weight="bold" fill="#065f46">JUnit Jupiter</text>
    <line x1="12" y1="36" x2="298" y2="36" stroke="#a7f3d0" stroke-width="1"/>
    <text x="15" y="54" font-size="10" font-weight="bold" fill="#047857">&bull; junit-jupiter-api (@Test, @DisplayName)</text>
    <text x="15" y="70" font-size="10" font-weight="bold" fill="#047857">&bull; junit-jupiter-params (@CsvSource, @EnumSource)</text>
    <text x="15" y="86" font-size="10" font-weight="bold" fill="#047857">&bull; junit-jupiter-engine (Execution core)</text>
    <text x="15" y="100" font-size="9" fill="#065f46" font-style="italic">Executes OceanCleanup2 Test Suite</text>
  </g>

  <!-- 3B: Vintage Engine -->
  <g transform="translate(370, 255)">
    <rect x="0" y="0" width="230" height="105" rx="8" fill="url(#grad_vintage)" stroke="#d97706" stroke-width="1.8" filter="url(#shadow1)"/>
    <rect x="12" y="10" width="95" height="20" rx="4" fill="#d97706"/>
    <text x="59" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">LEGACY</text>
    <text x="115" y="25" font-size="12" font-weight="bold" fill="#92400e">JUnit Vintage</text>
    <line x1="12" y1="36" x2="218" y2="36" stroke="#fde68a" stroke-width="1"/>
    <text x="15" y="55" font-size="10" fill="#78350f">&bull; junit-vintage-engine</text>
    <text x="15" y="73" font-size="10" fill="#78350f">&bull; Runs JUnit 3 &amp; JUnit 4 tests</text>
    <text x="15" y="93" font-size="9" fill="#92400e" font-style="italic">Ensures backwards compatibility</text>
  </g>

  <!-- 3C: Third Party Engines -->
  <g transform="translate(620, 255)">
    <rect x="0" y="0" width="200" height="105" rx="8" fill="url(#grad_third)" stroke="#7c3aed" stroke-width="1.8" filter="url(#shadow1)"/>
    <rect x="12" y="10" width="85" height="20" rx="4" fill="#7c3aed"/>
    <text x="54" y="24" font-size="9.5" font-weight="bold" fill="#ffffff" text-anchor="middle">EXTENSIBLE</text>
    <text x="105" y="25" font-size="12" font-weight="bold" fill="#5b21b6">Third Party</text>
    <line x1="12" y1="36" x2="188" y2="36" stroke="#ddd6fe" stroke-width="1"/>
    <text x="15" y="55" font-size="10" fill="#4c1d95">&bull; Spock Framework</text>
    <text x="15" y="73" font-size="10" fill="#4c1d95">&bull; Cucumber / jqwik</text>
    <text x="15" y="93" font-size="9" fill="#5b21b6" font-style="italic">Custom TestEngine Plugins</text>
  </g>
</svg>'''

with open(os.path.join(output_dir, "diagram_1_junit5_architecture.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_1)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 2: JUnit 5 Lifecycle Flowchart
# -------------------------------------------------------------------------------------------------
diagram_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 330" width="100%" height="330" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow2" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.07"/>
    </filter>
    <marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e3a8a"/>
    </marker>
    <marker id="arr2_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#059669"/>
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="12" width="820" height="34" rx="6" fill="#1e293b"/>
  <text x="430" y="34" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">
    JUNIT 5 METHOD LIFECYCLE &amp; ISOLATION EXECUTION WORKFLOW
  </text>

  <!-- Step 1: @BeforeAll -->
  <g transform="translate(30, 65)">
    <rect x="0" y="0" width="135" height="85" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" filter="url(#shadow2)"/>
    <rect x="15" y="8" width="105" height="22" rx="4" fill="#3b82f6"/>
    <text x="67" y="23" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">@BeforeAll</text>
    <text x="67" y="47" font-size="9.5" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Static Class Setup</text>
    <text x="67" y="63" font-size="8.5" fill="#475569" text-anchor="middle">Executes ONCE</text>
    <text x="67" y="75" font-size="8.5" fill="#64748b" text-anchor="middle">before any tests</text>
  </g>

  <!-- Arrow 1 -> 2 -->
  <line x1="167" y1="107" x2="198" y2="107" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr2)"/>

  <!-- Step 2: Instance Creation -->
  <g transform="translate(200, 65)">
    <rect x="0" y="0" width="135" height="85" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.8" stroke-dasharray="4 3" filter="url(#shadow2)"/>
    <rect x="15" y="8" width="105" height="22" rx="4" fill="#64748b"/>
    <text x="67" y="23" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">new TestClass()</text>
    <text x="67" y="47" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">Fresh Instance</text>
    <text x="67" y="63" font-size="8.5" fill="#475569" text-anchor="middle">PER_METHOD</text>
    <text x="67" y="75" font-size="8.5" fill="#64748b" text-anchor="middle">Isolation Guarantee</text>
  </g>

  <!-- Arrow 2 -> 3 -->
  <line x1="337" y1="107" x2="368" y2="107" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr2)"/>

  <!-- Step 3: @BeforeEach -->
  <g transform="translate(370, 65)">
    <rect x="0" y="0" width="135" height="85" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8" filter="url(#shadow2)"/>
    <rect x="15" y="8" width="105" height="22" rx="4" fill="#10b981"/>
    <text x="67" y="23" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">@BeforeEach</text>
    <text x="67" y="47" font-size="9.5" font-weight="bold" fill="#065f46" text-anchor="middle">Fixture Setup</text>
    <text x="67" y="63" font-size="8.5" fill="#047857" text-anchor="middle">Runs before</text>
    <text x="67" y="75" font-size="8.5" fill="#047857" text-anchor="middle">EACH @Test</text>
  </g>

  <!-- Arrow 3 -> 4 -->
  <line x1="507" y1="107" x2="538" y2="107" stroke="#059669" stroke-width="2" marker-end="url(#arr2_green)"/>

  <!-- Step 4: @Test Execution -->
  <g transform="translate(540, 55)">
    <rect x="0" y="0" width="145" height="105" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2.2" filter="url(#shadow2)"/>
    <rect x="15" y="8" width="115" height="24" rx="4" fill="#16a34a"/>
    <text x="72" y="24" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">@Test Execution</text>
    <text x="72" y="50" font-size="9.5" font-weight="bold" fill="#166534" text-anchor="middle">Assertions &amp; Logic</text>
    <text x="72" y="68" font-size="8.5" fill="#15803d" text-anchor="middle">&bull; assertAll()</text>
    <text x="72" y="82" font-size="8.5" fill="#15803d" text-anchor="middle">&bull; assertThrows()</text>
    <text x="72" y="96" font-size="8.5" fill="#15803d" text-anchor="middle">&bull; @ParameterizedTest</text>
  </g>

  <!-- Arrow 4 -> 5 -->
  <line x1="687" y1="107" x2="718" y2="107" stroke="#1e3a8a" stroke-width="2" marker-end="url(#arr2)"/>

  <!-- Step 5: @AfterEach -->
  <g transform="translate(720, 65)">
    <rect x="0" y="0" width="115" height="85" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8" filter="url(#shadow2)"/>
    <rect x="10" y="8" width="95" height="22" rx="4" fill="#ef4444"/>
    <text x="57" y="23" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">@AfterEach</text>
    <text x="57" y="47" font-size="9.5" font-weight="bold" fill="#991b1b" text-anchor="middle">Teardown</text>
    <text x="57" y="63" font-size="8.5" fill="#b91c1c" text-anchor="middle">Resets state</text>
    <text x="57" y="75" font-size="8.5" fill="#b91c1c" text-anchor="middle">per test</text>
  </g>

  <!-- Loopback arrow for subsequent tests -->
  <path d="M 777 152 L 777 195 L 267 195 L 267 152" fill="none" stroke="#2563eb" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#arr2)"/>
  <rect x="420" y="185" width="200" height="20" rx="4" fill="#dbeafe"/>
  <text x="520" y="199" font-size="9" font-weight="bold" fill="#1e40af" text-anchor="middle">Loop for next @Test method in class</text>

  <!-- Final Step: @AfterAll -->
  <g transform="translate(350, 230)">
    <rect x="0" y="0" width="160" height="75" rx="8" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.8" filter="url(#shadow2)"/>
    <rect x="15" y="8" width="130" height="22" rx="4" fill="#a855f7"/>
    <text x="80" y="23" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">@AfterAll</text>
    <text x="80" y="46" font-size="9.5" font-weight="bold" fill="#6b21a8" text-anchor="middle">Global Class Cleanup</text>
    <text x="80" y="62" font-size="8.5" fill="#7e22ce" text-anchor="middle">Executes ONCE after all tests</text>
  </g>

  <!-- Arrow down to AfterAll -->
  <line x1="777" y1="195" x2="777" y2="265" stroke="#a855f7" stroke-width="2"/>
  <line x1="777" y1="265" x2="512" y2="265" stroke="#a855f7" stroke-width="2" marker-end="url(#arr2)"/>
  <text x="645" y="258" font-size="8.5" font-weight="bold" fill="#6b21a8">When all tests finish</text>
</svg>'''

with open(os.path.join(output_dir, "diagram_2_junit5_lifecycle.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_2)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 3: OceanCleanup2 UML Class & Subsystem Architecture
# -------------------------------------------------------------------------------------------------
diagram_3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 400" width="100%" height="400" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow3" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0284c7"/>
    </marker>
    <marker id="arr3_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
  </defs>

  <!-- Title -->
  <rect x="20" y="10" width="820" height="34" rx="6" fill="#0284c7"/>
  <text x="430" y="32" font-size="13" font-weight="bold" fill="#ffffff" text-anchor="middle">
    OCEANCLEANUP2 CORE DOMAIN ENTITY &amp; TESTING SERVICE ARCHITECTURE
  </text>

  <!-- CENTER: Player Entity -->
  <g transform="translate(340, 58)">
    <rect x="0" y="0" width="180" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="180" height="26" rx="6" fill="#2563eb"/>
    <text x="90" y="18" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&laquo;Entity&raquo; Player</text>
    <text x="10" y="44" font-size="9" fill="#1e3a8a">- username: String</text>
    <text x="10" y="58" font-size="9" fill="#1e3a8a">- gold: int</text>
    <text x="10" y="72" font-size="9" fill="#1e3a8a">- energy: double (0..100)</text>
    <text x="10" y="86" font-size="9" fill="#1e3a8a">- score: int</text>
    <text x="10" y="100" font-size="9" fill="#1e3a8a">- boatLevel: int (1..4)</text>
    <text x="10" y="114" font-size="9" fill="#1e3a8a">- trashInventory: List</text>
    <text x="10" y="128" font-size="9" fill="#1e3a8a">- activeCompanion: Creature</text>
    <line x1="0" y1="134" x2="180" y2="134" stroke="#bfdbfe" stroke-width="1"/>
    <text x="10" y="145" font-size="8.5" fill="#1d4ed8" font-style="italic">getters / mutators</text>
  </g>

  <!-- LEFT TOP: BoatProgressionService -->
  <g transform="translate(40, 58)">
    <rect x="0" y="0" width="240" height="110" rx="8" fill="#f8fafc" stroke="#334155" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="240" height="24" rx="6" fill="#334155"/>
    <text x="120" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">BoatProgressionService</text>
    <text x="10" y="42" font-size="8.5" fill="#0f172a">+ getBoatLevel(level: int): BoatLevel</text>
    <text x="10" y="57" font-size="8.5" fill="#0f172a">+ canUpgrade(player: Player): boolean</text>
    <text x="10" y="72" font-size="8.5" fill="#0f172a">+ upgradeBoat(player: Player): BoatLevel</text>
    <text x="10" y="87" font-size="8.5" fill="#0f172a">+ getCapacityForPlayer(): int (20..120)</text>
    <text x="10" y="102" font-size="8.5" fill="#dc2626" font-weight="bold">&bull; Throws: MaxLevelReachedException</text>
  </g>
  <line x1="280" y1="113" x2="338" y2="113" stroke="#0284c7" stroke-width="2" marker-end="url(#arr3)"/>

  <!-- RIGHT TOP: EconomyAndRecyclingService -->
  <g transform="translate(580, 58)">
    <rect x="0" y="0" width="240" height="110" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="240" height="24" rx="6" fill="#16a34a"/>
    <text x="120" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">EconomyAndRecyclingService</text>
    <text x="10" y="42" font-size="8.5" fill="#14532d">+ recycleAllTrash(player: Player): int</text>
    <text x="10" y="57" font-size="8.5" fill="#14532d">+ purchaseFood(player: Player): boolean</text>
    <text x="10" y="72" font-size="8.5" fill="#14532d">+ restAndSleep(player: Player): void</text>
    <text x="10" y="87" font-size="8.5" fill="#14532d">+ applyEnergyDrain(player, dt): void</text>
    <text x="10" y="102" font-size="8.5" fill="#dc2626" font-weight="bold">&bull; Throws: InsufficientFundsException</text>
  </g>
  <line x1="520" y1="113" x2="578" y2="113" stroke="#0284c7" stroke-width="2" marker-end="url(#arr3)"/>

  <!-- LEFT BOTTOM: TrashCollectionService -->
  <g transform="translate(40, 230)">
    <rect x="0" y="0" width="240" height="110" rx="8" fill="#fefce8" stroke="#ca8a04" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="240" height="24" rx="6" fill="#ca8a04"/>
    <text x="120" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">TrashCollectionService</text>
    <text x="10" y="42" font-size="8.5" fill="#713f12">+ collectTrash(Player, TrashItem): boolean</text>
    <text x="10" y="57" font-size="8.5" fill="#713f12">+ calculateTotalScore(List): int</text>
    <text x="10" y="72" font-size="8.5" fill="#713f12">+ calculateTotalWeight(List): double</text>
    <text x="10" y="87" font-size="8.5" fill="#713f12">+ isWithinReelRadius(x, z, item, r): bool</text>
    <text x="10" y="102" font-size="8.5" fill="#dc2626" font-weight="bold">&bull; Throws: InventoryFullException</text>
  </g>
  <line x1="280" y1="260" x2="350" y2="208" stroke="#0284c7" stroke-width="2" marker-end="url(#arr3)"/>

  <!-- RIGHT BOTTOM: WildlifeRescueService -->
  <g transform="translate(580, 230)">
    <rect x="0" y="0" width="240" height="110" rx="8" fill="#faf5ff" stroke="#9333ea" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="240" height="24" rx="6" fill="#9333ea"/>
    <text x="120" y="17" font-size="10.5" font-weight="bold" fill="#ffffff" text-anchor="middle">WildlifeRescueService</text>
    <text x="10" y="42" font-size="8.5" fill="#581c87">+ attemptRescue(p, creature, dist): bool</text>
    <text x="10" y="57" font-size="8.5" fill="#581c87">+ assignCompanion(p, creature): bool</text>
    <text x="10" y="72" font-size="8.5" fill="#581c87">+ dismissCompanion(p: Player): void</text>
    <text x="10" y="87" font-size="8.5" fill="#581c87">+ Hitbox Radius = scale * 4.0</text>
    <text x="10" y="102" font-size="8.5" fill="#581c87">&bull; Species: Turtle, Dolphin, Whale, Ray</text>
  </g>
  <line x1="580" y1="260" x2="510" y2="208" stroke="#0284c7" stroke-width="2" marker-end="url(#arr3)"/>

  <!-- BOTTOM CENTER: GameStateManager & DayNight -->
  <g transform="translate(310, 255)">
    <rect x="0" y="0" width="240" height="85" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.8" filter="url(#shadow3)"/>
    <rect x="0" y="0" width="240" height="22" rx="6" fill="#475569"/>
    <text x="120" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GameStateManager &amp; DayNight</text>
    <text x="10" y="38" font-size="8.5" fill="#1e293b">&bull; FSM: LOADING &rarr; PLAYING &harr; PAUSED</text>
    <text x="10" y="52" font-size="8.5" fill="#dc2626" font-weight="bold">&bull; Throws: InvalidGameStateException</text>
    <text x="10" y="66" font-size="8.5" fill="#1e293b">&bull; DayNight: 24h solar curve, 60x speed</text>
    <text x="10" y="79" font-size="8.5" fill="#1e293b">&bull; Performance Timeout: 100k ticks &lt; 1s</text>
  </g>
  <line x1="430" y1="255" x2="430" y2="210" stroke="#0284c7" stroke-width="2" marker-end="url(#arr3)"/>
</svg>'''

with open(os.path.join(output_dir, "diagram_3_oceancleanup_architecture.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_3)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 4: GameState Finite State Machine (FSM) Diagram
# -------------------------------------------------------------------------------------------------
diagram_4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%" height="300" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow4" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr4_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
    <marker id="arr4_blue" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#2563eb"/>
    </marker>
    <marker id="arr4_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
  </defs>

  <!-- Title -->
  <rect x="20" y="10" width="820" height="32" rx="6" fill="#1e293b"/>
  <text x="430" y="31" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">
    GAME STATE FINITE STATE MACHINE (FSM) &amp; ILLEGAL TRANSITION TRAPS
  </text>

  <!-- Initial Node -->
  <circle cx="60" cy="115" r="14" fill="#0f172a"/>
  <line x1="74" y1="115" x2="118" y2="115" stroke="#2563eb" stroke-width="2.2" marker-end="url(#arr4_blue)"/>

  <!-- State 1: LOADING -->
  <g transform="translate(120, 85)">
    <rect x="0" y="0" width="125" height="60" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2" filter="url(#shadow4)"/>
    <text x="62" y="27" font-size="12" font-weight="bold" fill="#1e3a8a" text-anchor="middle">LOADING</text>
    <text x="62" y="45" font-size="9" fill="#2563eb" text-anchor="middle">Initial 3D Assets</text>
  </g>

  <!-- LOADING -> PLAYING -->
  <line x1="245" y1="115" x2="318" y2="115" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr4_green)"/>
  <text x="282" y="105" font-size="9" font-weight="bold" fill="#16a34a" text-anchor="middle">assetsLoaded()</text>

  <!-- State 2: PLAYING -->
  <g transform="translate(320, 85)">
    <rect x="0" y="0" width="140" height="60" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2.2" filter="url(#shadow4)"/>
    <text x="70" y="27" font-size="12" font-weight="bold" fill="#065f46" text-anchor="middle">PLAYING</text>
    <text x="70" y="45" font-size="9" fill="#059669" text-anchor="middle">Active Cleanup Loop</text>
  </g>

  <!-- PLAYING <-> PAUSED -->
  <!-- Top: PLAYING -> PAUSED -->
  <path d="M 460 100 L 538 100" fill="none" stroke="#2563eb" stroke-width="2" marker-end="url(#arr4_blue)"/>
  <text x="500" y="93" font-size="8.5" font-weight="bold" fill="#2563eb" text-anchor="middle">pause() [P Key]</text>

  <!-- Bottom: PAUSED -> PLAYING -->
  <path d="M 540 130 L 462 130" fill="none" stroke="#16a34a" stroke-width="2" marker-end="url(#arr4_green)"/>
  <text x="500" y="145" font-size="8.5" font-weight="bold" fill="#16a34a" text-anchor="middle">resume()</text>

  <!-- State 3: PAUSED -->
  <g transform="translate(540, 85)">
    <rect x="0" y="0" width="130" height="60" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2" filter="url(#shadow4)"/>
    <text x="65" y="27" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">PAUSED</text>
    <text x="65" y="45" font-size="9" fill="#b45309" text-anchor="middle">Physics Frozen</text>
  </g>

  <!-- PLAYING -> GAMEOVER -->
  <path d="M 390 145 L 390 220 L 538 220" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr4_red)"/>
  <text x="440" y="213" font-size="8.5" font-weight="bold" fill="#dc2626">energyDepleted() / quit()</text>

  <!-- State 4: GAMEOVER -->
  <g transform="translate(540, 195)">
    <rect x="0" y="0" width="130" height="60" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2" filter="url(#shadow4)"/>
    <text x="65" y="27" font-size="12" font-weight="bold" fill="#991b1b" text-anchor="middle">GAMEOVER</text>
    <text x="65" y="45" font-size="9" fill="#b91c1c" text-anchor="middle">Final Score Summary</text>
  </g>

  <!-- GAMEOVER -> PLAYING (Restart) -->
  <path d="M 540 240 L 350 240 L 350 147" fill="none" stroke="#16a34a" stroke-width="2" stroke-dasharray="4 3" marker-end="url(#arr4_green)"/>
  <text x="430" y="255" font-size="8.5" font-weight="bold" fill="#16a34a">restart() [Clean session]</text>

  <!-- ILLEGAL TRANSITIONS (Red curved lines with cross) -->
  <path d="M 180 85 Q 360 40 540 85" fill="none" stroke="#dc2626" stroke-width="2" stroke-dasharray="4 4" marker-end="url(#arr4_red)"/>
  <rect x="300" y="45" width="200" height="20" rx="4" fill="#fee2e2" stroke="#f87171"/>
  <text x="400" y="58" font-size="8" font-weight="bold" fill="#991b1b" text-anchor="middle">&#10006; ILLEGAL: LOADING &rarr; PAUSED</text>

  <!-- LEGEND -->
  <g transform="translate(710, 85)">
    <rect x="0" y="0" width="130" height="170" rx="6" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.2"/>
    <text x="15" y="20" font-size="10" font-weight="bold" fill="#0f172a">FSM Legend</text>
    <line x1="12" y1="28" x2="118" y2="28" stroke="#cbd5e1"/>
    <line x1="15" y1="45" x2="40" y2="45" stroke="#16a34a" stroke-width="2.5"/>
    <text x="48" y="48" font-size="8.5" fill="#334155">Valid Normal</text>
    <line x1="15" y1="65" x2="40" y2="65" stroke="#2563eb" stroke-width="2.5"/>
    <text x="48" y="68" font-size="8.5" fill="#334155">Pause / Resume</text>
    <line x1="15" y1="85" x2="40" y2="85" stroke="#dc2626" stroke-width="2.5"/>
    <text x="48" y="88" font-size="8.5" fill="#334155">Terminal Flow</text>
    <line x1="15" y1="105" x2="40" y2="105" stroke="#dc2626" stroke-width="2" stroke-dasharray="3 3"/>
    <text x="48" y="108" font-size="8.5" fill="#dc2626" font-weight="bold">Illegal Trap</text>
    <text x="12" y="130" font-size="8" fill="#475569">Tested with:</text>
    <text x="12" y="145" font-size="8" font-family="monospace" fill="#0284c7">@ParameterizedTest</text>
    <text x="12" y="158" font-size="8" font-family="monospace" fill="#0284c7">assertThrows()</text>
  </g>
</svg>'''

with open(os.path.join(output_dir, "diagram_4_gamestate_fsm.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_4)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 5: Day/Night Celestial Sun Elevation & Intensity Curves
# -------------------------------------------------------------------------------------------------
diagram_5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 300" width="100%" height="300" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow5" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <linearGradient id="dayGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#fef08a" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="nightGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#0f172a" stop-opacity="0.05"/>
    </linearGradient>
  </defs>

  <!-- Title -->
  <rect x="20" y="10" width="820" height="32" rx="6" fill="#0f172a"/>
  <text x="430" y="31" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">
    MATHEMATICAL 24-HOUR CELESTIAL SUN ELEVATION &amp; LIGHT INTENSITY MODEL
  </text>

  <!-- Background Zones -->
  <!-- Night: 0h to 6h (x=70 to 245) -->
  <rect x="70" y="60" width="175" height="190" fill="url(#nightGrad)"/>
  <!-- Day: 6h to 18h (x=245 to 595) -->
  <rect x="245" y="60" width="350" height="190" fill="url(#dayGrad)"/>
  <!-- Night: 18h to 24h (x=595 to 770) -->
  <rect x="595" y="60" width="175" height="190" fill="url(#nightGrad)"/>

  <!-- Grid & Axes -->
  <!-- Zero line (Horizon) at y=190 -->
  <line x1="70" y1="190" x2="770" y2="190" stroke="#475569" stroke-width="1.8"/>
  <text x="25" y="194" font-size="10" font-weight="bold" fill="#475569">0.0 (Horizon)</text>

  <!-- Peak line at y=80 (pi/2 = 1.57 rad) -->
  <line x1="70" y1="80" x2="770" y2="80" stroke="#cbd5e1" stroke-dasharray="4 4"/>
  <text x="15" y="84" font-size="9.5" fill="#0284c7">&pi;/2 (Noon)</text>

  <!-- Clamp Floor line at y=210 (-0.2 rad) -->
  <line x1="70" y1="210" x2="770" y2="210" stroke="#f87171" stroke-dasharray="3 3"/>
  <text x="10" y="214" font-size="9.5" fill="#dc2626">-0.2 (Clamp)</text>

  <!-- Vertical Hour Markers -->
  <!-- 0h Midnight -->
  <line x1="70" y1="60" x2="70" y2="250" stroke="#cbd5e1"/>
  <text x="70" y="265" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">0:00 (Midnight)</text>

  <!-- 6h Sunrise -->
  <line x1="245" y1="60" x2="245" y2="250" stroke="#eab308" stroke-width="1.5"/>
  <text x="245" y="265" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">6:00 (Sunrise)</text>

  <!-- 12h Noon -->
  <line x1="420" y1="60" x2="420" y2="250" stroke="#eab308" stroke-width="1.5"/>
  <text x="420" y="265" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">12:00 (Solar Noon)</text>

  <!-- 18h Sunset -->
  <line x1="595" y1="60" x2="595" y2="250" stroke="#eab308" stroke-width="1.5"/>
  <text x="595" y="265" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">18:00 (Sunset)</text>

  <!-- 24h Midnight -->
  <line x1="770" y1="60" x2="770" y2="250" stroke="#cbd5e1"/>
  <text x="770" y="265" font-size="10" font-weight="bold" fill="#334155" text-anchor="middle">24:00 (Rollover)</text>

  <!-- SINE ELEVATION CURVE -->
  <!-- Clamped at -0.2 (y=210) between 0h-6h, rises from 6h to 12h (y=80), drops to 18h, clamped 18h-24h -->
  <path d="M 70 210 L 245 210 C 290 180, 360 80, 420 80 C 480 80, 550 180, 595 210 L 770 210" 
        fill="none" stroke="#2563eb" stroke-width="3"/>

  <!-- SOLAR INTENSITY CURVE (Gold) -->
  <path d="M 70 190 L 245 190 C 265 190, 280 100, 420 90 C 560 100, 575 190, 595 190 L 770 190" 
        fill="none" stroke="#eab308" stroke-width="2" stroke-dasharray="5 3"/>

  <!-- Markers & Callouts -->
  <circle cx="420" cy="80" r="5" fill="#f59e0b"/>
  <text x="420" y="72" font-size="9" font-weight="bold" fill="#b45309" text-anchor="middle">Peak Intensity: 1.6 | Elevation: &pi;/2</text>

  <circle cx="245" cy="190" r="4" fill="#0284c7"/>
  <circle cx="595" cy="190" r="4" fill="#0284c7"/>

  <!-- Legend Card -->
  <g transform="translate(610, 70)">
    <rect x="0" y="0" width="180" height="75" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.2" filter="url(#shadow5)"/>
    <line x1="12" y1="20" x2="35" y2="20" stroke="#2563eb" stroke-width="3"/>
    <text x="42" y="23" font-size="8.5" font-weight="bold" fill="#1e3a8a">Sun Elevation Curve</text>
    <line x1="12" y1="38" x2="35" y2="38" stroke="#eab308" stroke-width="2" stroke-dasharray="4 2"/>
    <text x="42" y="41" font-size="8.5" font-weight="bold" fill="#b45309">Solar Intensity (I)</text>
    <line x1="12" y1="56" x2="35" y2="56" stroke="#f87171" stroke-dasharray="3 2"/>
    <text x="42" y="59" font-size="8.5" fill="#dc2626">Artifact Clamp (-0.2)</text>
  </g>
</svg>'''

with open(os.path.join(output_dir, "diagram_5_daynight_curves.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_5)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 6: Test Automation CI & Maven Surefire Pipeline
# -------------------------------------------------------------------------------------------------
diagram_6 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 260" width="100%" height="260" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow6" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
    <marker id="arr6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0284c7"/>
    </marker>
  </defs>

  <rect x="20" y="10" width="820" height="32" rx="6" fill="#1e293b"/>
  <text x="430" y="31" font-size="12.5" font-weight="bold" fill="#ffffff" text-anchor="middle">
    AUTOMATED TEST EXECUTION PIPELINE (MAVEN + JUNIT 5 SUREFIRE)
  </text>

  <!-- Step 1: Java Sources -->
  <g transform="translate(25, 65)">
    <rect x="0" y="0" width="135" height="150" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.8" filter="url(#shadow6)"/>
    <rect x="0" y="0" width="135" height="24" rx="6" fill="#64748b"/>
    <text x="67" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">1. Source Modules</text>
    <text x="10" y="44" font-size="9" fill="#1e293b">&bull; 15 Java Classes</text>
    <text x="10" y="62" font-size="9" fill="#1e293b">&bull; 6 Service Layers</text>
    <text x="10" y="80" font-size="9" fill="#1e293b">&bull; 4 Model Entities</text>
    <text x="10" y="98" font-size="9" fill="#1e293b">&bull; 4 Custom Exceptions</text>
    <text x="10" y="125" font-size="8.5" fill="#64748b" font-style="italic">src/main/java</text>
  </g>
  <line x1="160" y1="140" x2="190" y2="140" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arr6)"/>

  <!-- Step 2: Maven Compiler -->
  <g transform="translate(195, 65)">
    <rect x="0" y="0" width="135" height="150" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8" filter="url(#shadow6)"/>
    <rect x="0" y="0" width="135" height="24" rx="6" fill="#3b82f6"/>
    <text x="67" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">2. Maven Compiler</text>
    <text x="10" y="44" font-size="9" fill="#1e3a8a">&bull; Java 21 Target</text>
    <text x="10" y="62" font-size="9" fill="#1e3a8a">&bull; debug symbols [on]</text>
    <text x="10" y="80" font-size="9" fill="#1e3a8a">&bull; UTF-8 Encoding</text>
    <text x="10" y="98" font-size="9" fill="#1e3a8a">&bull; Incremental checks</text>
    <text x="10" y="125" font-size="8.5" fill="#3b82f6" font-style="italic">target/classes</text>
  </g>
  <line x1="330" y1="140" x2="360" y2="140" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arr6)"/>

  <!-- Step 3: Test Discovery -->
  <g transform="translate(365, 65)">
    <rect x="0" y="0" width="145" height="150" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8" filter="url(#shadow6)"/>
    <rect x="0" y="0" width="145" height="24" rx="6" fill="#10b981"/>
    <text x="72" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">3. Jupiter Discovery</text>
    <text x="10" y="44" font-size="9" fill="#065f46">&bull; 6 Test Classes</text>
    <text x="10" y="62" font-size="9" fill="#065f46">&bull; Master @Suite</text>
    <text x="10" y="80" font-size="9" fill="#065f46">&bull; @ParameterizedTest</text>
    <text x="10" y="98" font-size="9" fill="#065f46">&bull; @Nested hierarchies</text>
    <text x="10" y="125" font-size="8.5" fill="#059669" font-style="italic">JUnit Platform</text>
  </g>
  <line x1="510" y1="140" x2="540" y2="140" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arr6)"/>

  <!-- Step 4: Surefire Execution -->
  <g transform="translate(545, 65)">
    <rect x="0" y="0" width="140" height="150" rx="8" fill="#fdf4ff" stroke="#a855f7" stroke-width="1.8" filter="url(#shadow6)"/>
    <rect x="0" y="0" width="140" height="24" rx="6" fill="#a855f7"/>
    <text x="70" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">4. Surefire Runner</text>
    <text x="10" y="44" font-size="9" fill="#581c87">&bull; 66 Tests Executed</text>
    <text x="10" y="62" font-size="9" fill="#581c87">&bull; 0 Failures</text>
    <text x="10" y="80" font-size="9" fill="#581c87">&bull; 0 Errors</text>
    <text x="10" y="98" font-size="9" fill="#581c87">&bull; 1 Skipped (@Disabled)</text>
    <text x="10" y="125" font-size="8.5" fill="#7e22ce" font-style="italic">Time: 42.37s</text>
  </g>
  <line x1="685" y1="140" x2="710" y2="140" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arr6)"/>

  <!-- Step 5: Reports Generated -->
  <g transform="translate(715, 65)">
    <rect x="0" y="0" width="125" height="150" rx="8" fill="#f0fdf4" stroke="#16a34a" stroke-width="2" filter="url(#shadow6)"/>
    <rect x="0" y="0" width="125" height="24" rx="6" fill="#16a34a"/>
    <text x="62" y="16" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">5. Test Reports</text>
    <text x="10" y="44" font-size="8.5" fill="#14532d">&bull; 14 Surefire XMLs</text>
    <text x="10" y="62" font-size="8.5" fill="#14532d">&bull; 14 TXT Logs</text>
    <text x="10" y="80" font-size="8.5" fill="#14532d">&bull; 100% Pass Rate</text>
    <rect x="8" y="100" width="108" height="26" rx="4" fill="#dcfce7" stroke="#86efac"/>
    <text x="62" y="117" font-size="10" font-weight="bold" fill="#15803d" text-anchor="middle">BUILD SUCCESS</text>
  </g>
</svg>'''

with open(os.path.join(output_dir, "diagram_6_test_automation_pipeline.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_6)

# -------------------------------------------------------------------------------------------------
# DIAGRAM 7: Test Execution KPI Dashboard Widget (SonarQube / Allure style)
# -------------------------------------------------------------------------------------------------
diagram_7 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 170" width="100%" height="170" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <filter id="shadow7" x="-5%" y="-5%" width="110%" height="115%" filterUnits="userSpaceOnUse">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.08"/>
    </filter>
  </defs>

  <rect x="0" y="0" width="860" height="170" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>

  <!-- Card 1: Total Tests -->
  <g transform="translate(25, 20)">
    <rect x="0" y="0" width="145" height="130" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow7)"/>
    <text x="72" y="32" font-size="11" font-weight="bold" fill="#64748b" text-anchor="middle">TOTAL TESTS</text>
    <text x="72" y="80" font-size="34" font-weight="bold" fill="#1e293b" text-anchor="middle">66</text>
    <rect x="25" y="95" width="95" height="20" rx="10" fill="#f1f5f9"/>
    <text x="72" y="109" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">Across 6 Suites</text>
  </g>

  <!-- Card 2: Passed Tests -->
  <g transform="translate(190, 20)">
    <rect x="0" y="0" width="145" height="130" rx="8" fill="#ffffff" stroke="#86efac" stroke-width="1.5" filter="url(#shadow7)"/>
    <text x="72" y="32" font-size="11" font-weight="bold" fill="#15803d" text-anchor="middle">PASSED</text>
    <text x="72" y="80" font-size="34" font-weight="bold" fill="#16a34a" text-anchor="middle">65</text>
    <rect x="25" y="95" width="95" height="20" rx="10" fill="#dcfce7"/>
    <text x="72" y="109" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">100% Active Pass</text>
  </g>

  <!-- Card 3: Failures & Errors -->
  <g transform="translate(355, 20)">
    <rect x="0" y="0" width="145" height="130" rx="8" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#shadow7)"/>
    <text x="72" y="32" font-size="11" font-weight="bold" fill="#dc2626" text-anchor="middle">FAILURES / ERRORS</text>
    <text x="72" y="80" font-size="34" font-weight="bold" fill="#0f172a" text-anchor="middle">0 / 0</text>
    <rect x="25" y="95" width="95" height="20" rx="10" fill="#f1f5f9"/>
    <text x="72" y="109" font-size="9" font-weight="bold" fill="#16a34a" text-anchor="middle">Zero Regressions</text>
  </g>

  <!-- Card 4: Skipped -->
  <g transform="translate(520, 20)">
    <rect x="0" y="0" width="145" height="130" rx="8" fill="#ffffff" stroke="#fde047" stroke-width="1.5" filter="url(#shadow7)"/>
    <text x="72" y="32" font-size="11" font-weight="bold" fill="#a16207" text-anchor="middle">SKIPPED</text>
    <text x="72" y="80" font-size="34" font-weight="bold" fill="#ca8a04" text-anchor="middle">1</text>
    <rect x="25" y="95" width="95" height="20" rx="10" fill="#fef9c3"/>
    <text x="72" y="109" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">@Disabled (v3.0)</text>
  </g>

  <!-- Card 5: Duration & Build Status -->
  <g transform="translate(685, 20)">
    <rect x="0" y="0" width="150" height="130" rx="8" fill="#f0fdf4" stroke="#4ade80" stroke-width="1.8" filter="url(#shadow7)"/>
    <text x="75" y="30" font-size="10" font-weight="bold" fill="#166534" text-anchor="middle">EXECUTION DURATION</text>
    <text x="75" y="65" font-size="22" font-weight="bold" fill="#15803d" text-anchor="middle">42.37 s</text>
    <rect x="15" y="85" width="120" height="32" rx="6" fill="#16a34a"/>
    <text x="75" y="105" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">&#10004; BUILD SUCCESS</text>
  </g>
</svg>'''

with open(os.path.join(output_dir, "diagram_7_execution_kpi_dashboard.svg"), "w", encoding="utf-8") as f:
    f.write(diagram_7)

print("Generated all 7 SVG diagrams successfully!")
