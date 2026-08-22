# 📁 src

- **Generated:** 2026-08-22 01:12
- **Total Files:** 63
- **Source:** `C:\Users\DELL\Downloads\server3\my-app\packages\mt5-admin\src`

---

## 📑 Table of Contents

1. [browser/mt5-admin-content-widget.tsx](#browser-mt5-admin-content-widget-tsx)
2. [browser/mt5-admin-contribution.ts](#browser-mt5-admin-contribution-ts)
3. [browser/mt5-admin-frontend-module.ts](#browser-mt5-admin-frontend-module-ts)
4. [browser/mt5-admin-tree-widget.tsx](#browser-mt5-admin-tree-widget-tsx)
5. [browser/mt5-admin-view-container.ts](#browser-mt5-admin-view-container-ts)
6. [browser/modules/api.ts](#browser-modules-api-ts)
7. [browser/modules/clients/ClientsPage.tsx](#browser-modules-clients-clientspage-tsx)
8. [browser/modules/data-feeds/DataFeedsPage.tsx](#browser-modules-data-feeds-datafeedspage-tsx)
9. [browser/modules/deals/DealsPage.tsx](#browser-modules-deals-dealspage-tsx)
10. [browser/modules/gateways/GatewaysPage.tsx](#browser-modules-gateways-gatewayspage-tsx)
11. [browser/modules/groups/GroupsPage.tsx](#browser-modules-groups-groupspage-tsx)
12. [browser/modules/groups/groupTypeUtils.ts](#browser-modules-groups-grouptypeutils-ts)
13. [browser/modules/groups/modal/GroupDraftContext.tsx](#browser-modules-groups-modal-groupdraftcontext-tsx)
14. [browser/modules/groups/modal/GroupSettingsModal.tsx](#browser-modules-groups-modal-groupsettingsmodal-tsx)
15. [browser/modules/groups/modal/tabs/CommissionsTab.tsx](#browser-modules-groups-modal-tabs-commissionstab-tsx)
16. [browser/modules/groups/modal/tabs/CommonTab.tsx](#browser-modules-groups-modal-tabs-commontab-tsx)
17. [browser/modules/groups/modal/tabs/CompanyTab.tsx](#browser-modules-groups-modal-tabs-companytab-tsx)
18. [browser/modules/groups/modal/tabs/GatewayTab.tsx](#browser-modules-groups-modal-tabs-gatewaytab-tsx)
19. [browser/modules/groups/modal/tabs/MarginTab.tsx](#browser-modules-groups-modal-tabs-margintab-tsx)
20. [browser/modules/groups/modal/tabs/NewsMailTab.tsx](#browser-modules-groups-modal-tabs-newsmailtab-tsx)
21. [browser/modules/groups/modal/tabs/PermissionsTab.tsx](#browser-modules-groups-modal-tabs-permissionstab-tsx)
22. [browser/modules/groups/modal/tabs/ReportsTab.tsx](#browser-modules-groups-modal-tabs-reportstab-tsx)
23. [browser/modules/groups/modal/tabs/SymbolsTab.tsx](#browser-modules-groups-modal-tabs-symbolstab-tsx)
24. [browser/modules/groups/modal/tabs/commissions/CommissionRuleDialog.tsx](#browser-modules-groups-modal-tabs-commissions-commissionruledialog-tsx)
25. [browser/modules/groups/modal/tabs/symbols/SymbolRuleDialog.tsx](#browser-modules-groups-modal-tabs-symbols-symbolruledialog-tsx)
26. [browser/modules/market-watch/MarketWatchPage.tsx](#browser-modules-market-watch-marketwatchpage-tsx)
27. [browser/modules/network-cluster/NetworkClusterPage.tsx](#browser-modules-network-cluster-networkclusterpage-tsx)
28. [browser/modules/orders/OrdersPage.tsx](#browser-modules-orders-orderspage-tsx)
29. [browser/modules/positions/ExposurePage.tsx](#browser-modules-positions-exposurepage-tsx)
30. [browser/modules/positions/MarginCallPage.tsx](#browser-modules-positions-margincallpage-tsx)
31. [browser/modules/positions/PositionsPage.tsx](#browser-modules-positions-positionspage-tsx)
32. [browser/modules/positions/SummaryPage.tsx](#browser-modules-positions-summarypage-tsx)
33. [browser/modules/routing/RoutingPage.tsx](#browser-modules-routing-routingpage-tsx)
34. [browser/modules/symbols/AllSymbolsPage.tsx](#browser-modules-symbols-allsymbolspage-tsx)
35. [browser/modules/symbols/SymbolFilterBar.tsx](#browser-modules-symbols-symbolfilterbar-tsx)
36. [browser/modules/symbols/SymbolFolderUtils.ts](#browser-modules-symbols-symbolfolderutils-ts)
37. [browser/modules/symbols/SymbolsContextMenu.tsx](#browser-modules-symbols-symbolscontextmenu-tsx)
38. [browser/modules/symbols/SymbolsPage.tsx](#browser-modules-symbols-symbolspage-tsx)
39. [browser/modules/symbols/SymbolsTable.tsx](#browser-modules-symbols-symbolstable-tsx)
40. [browser/modules/symbols/SymbolsTree.tsx](#browser-modules-symbols-symbolstree-tsx)
41. [browser/modules/symbols/SymbolsTreePage.tsx](#browser-modules-symbols-symbolstreepage-tsx)
42. [browser/modules/symbols/ImportWizard/ConnectStep.tsx](#browser-modules-symbols-importwizard-connectstep-tsx)
43. [browser/modules/symbols/ImportWizard/ImportSummary.tsx](#browser-modules-symbols-importwizard-importsummary-tsx)
44. [browser/modules/symbols/ImportWizard/ImportWizard.tsx](#browser-modules-symbols-importwizard-importwizard-tsx)
45. [browser/modules/symbols/ImportWizard/SelectSymbolsStep.tsx](#browser-modules-symbols-importwizard-selectsymbolsstep-tsx)
46. [browser/modules/symbols/modal/BulkEditBanner.tsx](#browser-modules-symbols-modal-bulkeditbanner-tsx)
47. [browser/modules/symbols/modal/SymbolDraftContext.tsx](#browser-modules-symbols-modal-symboldraftcontext-tsx)
48. [browser/modules/symbols/modal/SymbolSettingsModal.tsx](#browser-modules-symbols-modal-symbolsettingsmodal-tsx)
49. [browser/modules/symbols/modal/tabs/BondsTab.tsx](#browser-modules-symbols-modal-tabs-bondstab-tsx)
50. [browser/modules/symbols/modal/tabs/CommonTab.tsx](#browser-modules-symbols-modal-tabs-commontab-tsx)
51. [browser/modules/symbols/modal/tabs/CurrencyTab.tsx](#browser-modules-symbols-modal-tabs-currencytab-tsx)
52. [browser/modules/symbols/modal/tabs/ExecutionTab.tsx](#browser-modules-symbols-modal-tabs-executiontab-tsx)
53. [browser/modules/symbols/modal/tabs/FuturesTab.tsx](#browser-modules-symbols-modal-tabs-futurestab-tsx)
54. [browser/modules/symbols/modal/tabs/MarginRatesTab.tsx](#browser-modules-symbols-modal-tabs-marginratestab-tsx)
55. [browser/modules/symbols/modal/tabs/MarginTab.tsx](#browser-modules-symbols-modal-tabs-margintab-tsx)
56. [browser/modules/symbols/modal/tabs/OptionsTab.tsx](#browser-modules-symbols-modal-tabs-optionstab-tsx)
57. [browser/modules/symbols/modal/tabs/QuotesTab.tsx](#browser-modules-symbols-modal-tabs-quotestab-tsx)
58. [browser/modules/symbols/modal/tabs/SessionsTab.tsx](#browser-modules-symbols-modal-tabs-sessionstab-tsx)
59. [browser/modules/symbols/modal/tabs/SwapsTab.tsx](#browser-modules-symbols-modal-tabs-swapstab-tsx)
60. [browser/modules/symbols/modal/tabs/TradeTab.tsx](#browser-modules-symbols-modal-tabs-tradetab-tsx)
61. [browser/modules/symbols/modal/tabs/sessions/DayScheduleEditor.tsx](#browser-modules-symbols-modal-tabs-sessions-dayscheduleeditor-tsx)
62. [browser/style/index.css](#browser-style-index-css)
63. [common/mt5-admin-tree.ts](#common-mt5-admin-tree-ts)

---

## 🌲 Project Structure

```
src/
├── browser/
│   ├── modules/
│   │   ├── api.ts
│   │   ├── clients/
│   │   │   └── ClientsPage.tsx
│   │   ├── data-feeds/
│   │   │   └── DataFeedsPage.tsx
│   │   ├── deals/
│   │   │   └── DealsPage.tsx
│   │   ├── gateways/
│   │   │   └── GatewaysPage.tsx
│   │   ├── groups/
│   │   │   ├── GroupsPage.tsx
│   │   │   ├── groupTypeUtils.ts
│   │   │   └── modal/
│   │   │       ├── GroupDraftContext.tsx
│   │   │       ├── GroupSettingsModal.tsx
│   │   │       └── tabs/
│   │   │           ├── commissions/
│   │   │           │   └── CommissionRuleDialog.tsx
│   │   │           ├── CommissionsTab.tsx
│   │   │           ├── CommonTab.tsx
│   │   │           ├── CompanyTab.tsx
│   │   │           ├── GatewayTab.tsx
│   │   │           ├── MarginTab.tsx
│   │   │           ├── NewsMailTab.tsx
│   │   │           ├── PermissionsTab.tsx
│   │   │           ├── ReportsTab.tsx
│   │   │           ├── symbols/
│   │   │           │   └── SymbolRuleDialog.tsx
│   │   │           └── SymbolsTab.tsx
│   │   ├── market-watch/
│   │   │   └── MarketWatchPage.tsx
│   │   ├── network-cluster/
│   │   │   └── NetworkClusterPage.tsx
│   │   ├── orders/
│   │   │   └── OrdersPage.tsx
│   │   ├── positions/
│   │   │   ├── ExposurePage.tsx
│   │   │   ├── MarginCallPage.tsx
│   │   │   ├── PositionsPage.tsx
│   │   │   └── SummaryPage.tsx
│   │   ├── routing/
│   │   │   └── RoutingPage.tsx
│   │   └── symbols/
│   │       ├── AllSymbolsPage.tsx
│   │       ├── ImportWizard/
│   │       │   ├── ConnectStep.tsx
│   │       │   ├── ImportSummary.tsx
│   │       │   ├── ImportWizard.tsx
│   │       │   └── SelectSymbolsStep.tsx
│   │       ├── modal/
│   │       │   ├── BulkEditBanner.tsx
│   │       │   ├── SymbolDraftContext.tsx
│   │       │   ├── SymbolSettingsModal.tsx
│   │       │   └── tabs/
│   │       │       ├── BondsTab.tsx
│   │       │       ├── CommonTab.tsx
│   │       │       ├── CurrencyTab.tsx
│   │       │       ├── ExecutionTab.tsx
│   │       │       ├── FuturesTab.tsx
│   │       │       ├── MarginRatesTab.tsx
│   │       │       ├── MarginTab.tsx
│   │       │       ├── OptionsTab.tsx
│   │       │       ├── QuotesTab.tsx
│   │       │       ├── sessions/
│   │       │       │   └── DayScheduleEditor.tsx
│   │       │       ├── SessionsTab.tsx
│   │       │       ├── SwapsTab.tsx
│   │       │       └── TradeTab.tsx
│   │       ├── SymbolFilterBar.tsx
│   │       ├── SymbolFolderUtils.ts
│   │       ├── SymbolsContextMenu.tsx
│   │       ├── SymbolsPage.tsx
│   │       ├── SymbolsTable.tsx
│   │       ├── SymbolsTree.tsx
│   │       └── SymbolsTreePage.tsx
│   ├── mt5-admin-content-widget.tsx
│   ├── mt5-admin-contribution.ts
│   ├── mt5-admin-frontend-module.ts
│   ├── mt5-admin-tree-widget.tsx
│   ├── mt5-admin-view-container.ts
│   └── style/
│       └── index.css
└── common/
    └── mt5-admin-tree.ts
```

---

## 📄 Files

<a id='browser-mt5-admin-content-widget-tsx'></a>
### 63. `browser/mt5-admin-content-widget.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { injectable, postConstruct } from '@theia/core/shared/inversify';
import { ReactWidget } from '@theia/core/lib/browser';

// Network Cluster
import { NetworkClusterOverview, NetworkServersPage, NetworkDataCentersPage, NetworkBackupPage } from './modules/network-cluster/NetworkClusterPage';
// Groups
import { GroupsOverviewPage } from './modules/groups/GroupsPage';
// Clients
import { ClientsPage } from './modules/clients/ClientsPage';
// Positions
import { PositionsPage } from './modules/positions/PositionsPage';
import { SummaryPage } from './modules/positions/SummaryPage';
import { ExposurePage } from './modules/positions/ExposurePage';
import { MarginCallPage } from './modules/positions/MarginCallPage';
// Orders
import { OrdersPage } from './modules/orders/OrdersPage';
// Deals
import { DealsPage } from './modules/deals/DealsPage';
// Gateways
import { GatewaysPage } from './modules/gateways/GatewaysPage';
// Data Feeds
import { DataFeedsPage } from './modules/data-feeds/DataFeedsPage';
// Routing
import { RoutingPage } from './modules/routing/RoutingPage';
// Symbols
import { SymbolsPage } from './modules/symbols/SymbolsPage';
// Market Watch (debug)
import { MarketWatchPage } from './modules/market-watch/MarketWatchPage';

@injectable()
export class Mt5AdminContentWidget extends ReactWidget {

    static createId(nodeId: string): string {
        return `mt5-admin-content:${nodeId}`;
    }

    protected nodeId: string = '';
    protected nodeLabel: string = '';
    protected filterPath: string = '';

    setFilterPath(path: string): void {
        this.filterPath = path;
        this.update();
    }

    initialize(nodeId: string, nodeLabel: string): void {
        this.nodeId = nodeId;
        this.nodeLabel = nodeLabel;
        this.id = Mt5AdminContentWidget.createId(nodeId);
        this.title.label = nodeLabel;
        this.title.caption = nodeLabel;
        this.title.closable = true;
        this.title.iconClass = `codicon codicon-${this.getIconForNode(nodeId)}`;
        this.addClass('mt5-admin-content-widget');
        this.update();
    }

    protected getIconForNode(id: string): string {
        const map: Record<string, string> = {
            'start-page': 'home',
            'network-cluster': 'server',
            'network-cluster.servers': 'server-environment',
            'network-cluster.data-centers': 'database',
            'network-cluster.backup': 'save',
            'groups': 'organization',
            'groups.settings': 'settings-gear',
            'groups.types': 'type-hierarchy',
            'groups.symbols': 'graph-line',
            'groups.permissions': 'lock',
            'allocations': 'list-selection',
            'clients-and-accounts': 'person',
            'clients-and-accounts.allocations': 'list-selection',
            'clients-and-accounts.clients': 'organization',
            'clients-and-accounts.managers': 'account',
            'clients-and-accounts.trading-accounts': 'credit-card',
            'positions': 'graph-scatter',
            'positions.open': 'graph-scatter',
            'positions.summary': 'list-flat',
            'positions.exposure': 'pie-chart',
            'positions.margin-call': 'warning',
            'positions.history': 'history',
            'orders': 'list-ordered',
            'orders.active': 'clock',
            'orders.history': 'history',
            'orders.create': 'add',
            'deals': 'pulse',
            'deals.list': 'list-unordered',
            'deals.search': 'search',
            'gateways': 'radio-tower',
            'gateways.list': 'radio-tower',
            'gateways.routing': 'git-merge',
            'data-feeds': 'broadcast',
            'data-feeds.sources': 'database',
            'data-feeds.news': 'rss',
            'routing': 'git-merge',
            'routing.rules': 'list-ordered',
            'routing.a-book': 'arrow-right',
            'routing.b-book': 'arrow-left',
            'routing.gateways': 'radio-tower',
            'symbols': 'symbol-namespace',
            'symbols.list': 'list-unordered',
            'symbols.create': 'add',
            'symbols.sessions': 'clock',
            'market-watch': 'eye',
        };
        return map[id] || 'server';
    }

    @postConstruct()
    protected postInit(): void { }

    /**
     * Each node ID maps to a DISTINCT React component / view.
     * Sub-nodes must render different content from their parent.
     */
    protected renderPage(nodeId: string): React.ReactNode {
        switch (nodeId) {
            // ── Network Cluster ──────────────────────────────────────
            case 'network-cluster':           return <NetworkClusterOverview />;
            case 'network-cluster.servers':   return <NetworkServersPage />;
            case 'network-cluster.data-centers': return <NetworkDataCentersPage />;
            case 'network-cluster.backup':    return <NetworkBackupPage />;

            // ── Groups ───────────────────────────────────────────────
            case 'groups':                    return <GroupsOverviewPage selectedPath={this.filterPath} />;

            // ── Clients / Accounts ───────────────────────────────────
            case 'clients-and-accounts':                       return <ClientsPage initialTab="accounts" />;
            case 'clients-and-accounts.allocations':          return <ClientsPage initialTab="allocations" />;
            case 'clients-and-accounts.clients':              return <ClientsPage initialTab="clients" />;
            case 'clients-and-accounts.managers':             return <ClientsPage initialTab="managers" />;
            case 'clients-and-accounts.trading-accounts':      return <ClientsPage initialTab="accounts" />;

            // ── Positions ────────────────────────────────────────────
            case 'positions':                 return <PositionsPage view="open" />;
            case 'positions.open':            return <PositionsPage view="open" />;
            case 'positions.summary':         return <SummaryPage />;
            case 'positions.exposure':        return <ExposurePage />;
            case 'positions.margin-call':     return <MarginCallPage />;
            case 'positions.history':         return <PositionsPage view="history" />;

            // ── Orders ───────────────────────────────────────────────
            case 'orders':                    return <OrdersPage view="active" />;
            case 'orders.active':             return <OrdersPage view="active" />;
            case 'orders.history':            return <OrdersPage view="history" />;
            case 'orders.create':             return <OrdersPage view="new" />;

            // ── Deals ────────────────────────────────────────────────
            case 'deals':                     return <DealsPage view="log" />;
            case 'deals.list':                return <DealsPage view="log" />;
            case 'deals.search':              return <DealsPage view="search" />;

            // ── Gateways ─────────────────────────────────────────────
            case 'gateways':                  return <GatewaysPage view="list" />;
            case 'gateways.list':             return <GatewaysPage view="list" />;
            case 'gateways.routing':          return <GatewaysPage view="routing" />;

            // ── Data Feeds ───────────────────────────────────────────
            case 'data-feeds':                return <DataFeedsPage view="sources" />;
            case 'data-feeds.sources':        return <DataFeedsPage view="sources" />;
            case 'data-feeds.news':           return <DataFeedsPage view="news" />;

            // ── Market Watch (debug) ─────────────────────────────────
            case 'market-watch':              return <MarketWatchPage />;

            // ── Routing ──────────────────────────────────────────────
            case 'routing':                   return <RoutingPage view="all" />;
            case 'routing.rules':             return <RoutingPage view="all" />;
            case 'routing.a-book':            return <RoutingPage view="a-book" />;
            case 'routing.b-book':            return <RoutingPage view="b-book" />;
            case 'routing.gateways':          return <RoutingPage view="gateways" />;

            // ── Symbols ──────────────────────────────────────────────
            case 'symbols':                   return <SymbolsPage selectedPath={this.filterPath} />;

            default: return this.renderPlaceholder(nodeId);
        }
    }

    protected renderPlaceholder(nodeId: string): React.ReactNode {
        return (
            <div className="mt5-admin-section-placeholder">
                <div className="mt5-admin-section-desc">
                    <strong>{this.nodeLabel}</strong> — This section is being implemented.
                </div>
                <div className="mt5-admin-section-wip">
                    <i className="codicon codicon-tools" style={{ marginRight: '8px' }} />
                    Connect to <code>localhost:8000</code> API.
                </div>
            </div>
        );
    }

    protected render(): React.ReactNode {
        return (
            <div className="mt5-admin-content-panel">
                <div className="mt5-admin-content-header">
                    <i className={`codicon codicon-${this.getIconForNode(this.nodeId)} mt5-admin-content-header-icon`} />
                    <h1 className="mt5-admin-content-title">{this.nodeLabel}</h1>
                </div>
                <div className="mt5-admin-content-body" style={{ padding: 0, display: 'flex', flexDirection: 'column', flex: 1, overflow: 'hidden' }}>
                    {this.renderPage(this.nodeId)}
                </div>
            </div>
        );
    }
}

```

---

<a id='browser-mt5-admin-contribution-ts'></a>
### 63. `browser/mt5-admin-contribution.ts`

```typescript
// @ts-nocheck
import { injectable, inject } from '@theia/core/shared/inversify';
import { AbstractViewContribution } from '@theia/core/lib/browser/shell/view-contribution';
import { Mt5AdminTreeWidget, MT5_ADMIN_TREE_WIDGET_ID } from './mt5-admin-tree-widget';
import {
    FrontendApplicationContribution,
    FrontendApplication,
    WidgetManager,
    ApplicationShell
} from '@theia/core/lib/browser';
import { CommandRegistry, Command } from '@theia/core/lib/common/command';
import { MenuModelRegistry } from '@theia/core/lib/common';
import { MT5_ADMIN_CONTAINER_ID } from './mt5-admin-view-container';
import { Mt5AdminContentWidget } from './mt5-admin-content-widget';

export namespace Mt5AdminCommands {
    export const OPEN_ADMIN: Command = {
        id: 'mt5-admin:open',
        label: 'MT5 Administrator'
    };

    export const OPEN_VIEW: Command = {
        id: 'mt5-admin:open-view',
        label: 'MT5 Admin: Open Section'
    };
}

@injectable()
export class Mt5AdminContribution
    extends AbstractViewContribution<Mt5AdminTreeWidget>
    implements FrontendApplicationContribution {

    @inject(WidgetManager)
    protected readonly widgetManager: WidgetManager;

    @inject(ApplicationShell)
    protected readonly shell: ApplicationShell;

    constructor() {
        super({
            viewContainerId: MT5_ADMIN_CONTAINER_ID,
            widgetId: MT5_ADMIN_TREE_WIDGET_ID,
            widgetName: 'MT5 Admin',
            defaultWidgetOptions: {
                area: 'left',
                rank: 600
            },
            toggleCommandId: 'mt5-admin:toggle',
            toggleKeybinding: 'ctrlcmd+shift+a'
        });
    }

    async initializeLayout(app: FrontendApplication): Promise<void> {
        await this.shell.revealWidget(MT5_ADMIN_CONTAINER_ID);
    }

    override registerCommands(commands: CommandRegistry): void {
        super.registerCommands(commands);

        commands.registerCommand(Mt5AdminCommands.OPEN_ADMIN, {
            execute: () => this.shell.revealWidget(MT5_ADMIN_CONTAINER_ID)
        });

        // Called by the tree widget when user clicks a node
        commands.registerCommand(Mt5AdminCommands.OPEN_VIEW, {
            execute: async (nodeId: string, nodeLabel: string) => {
                let targetNodeId = nodeId;
                let filterPath = '';
                if (nodeId.startsWith('groups:')) {
                    targetNodeId = 'groups';
                    filterPath = nodeId.substring(7);
                } else if (nodeId.startsWith('symbols:')) {
                    targetNodeId = 'symbols';
                    filterPath = nodeId.substring(8);
                }

                const widgetId = Mt5AdminContentWidget.createId(targetNodeId);

                // Check if already open
                const existing = this.shell.getWidgetById(widgetId) as Mt5AdminContentWidget;
                if (existing) {
                    this.shell.activateWidget(widgetId);
                    if (targetNodeId === 'groups' || targetNodeId === 'symbols') {
                        existing.setFilterPath(filterPath);
                    }
                    return;
                }

                // Create a fresh content widget for this section
                const widget = new Mt5AdminContentWidget();
                widget.initialize(targetNodeId, targetNodeId === 'groups' ? 'Groups' : targetNodeId === 'symbols' ? 'Symbols' : nodeLabel);
                
                if (targetNodeId === 'groups' || targetNodeId === 'symbols') {
                    widget.setFilterPath(filterPath);
                }

                this.shell.addWidget(widget, {
                    area: 'main',
                    mode: 'tab-after'
                });
                this.shell.activateWidget(widgetId);
            }
        });
    }

    override registerMenus(menus: MenuModelRegistry): void {
        super.registerMenus(menus);
    }
}

```

---

<a id='browser-mt5-admin-frontend-module-ts'></a>
### 63. `browser/mt5-admin-frontend-module.ts`

```typescript
// @ts-nocheck
import { ContainerModule } from '@theia/core/shared/inversify';
import { Mt5AdminTreeWidget, MT5_ADMIN_TREE_WIDGET_ID } from './mt5-admin-tree-widget';
import { Mt5AdminContribution } from './mt5-admin-contribution';
import { Mt5AdminViewContainerFactory } from './mt5-admin-view-container';
import {
    bindViewContribution,
    FrontendApplicationContribution,
    WidgetFactory
} from '@theia/core/lib/browser';
import './style/index.css';

export default new ContainerModule(bind => {
    // Register the sidebar contribution (activity bar panel + commands)
    bindViewContribution(bind, Mt5AdminContribution);
    bind(FrontendApplicationContribution).toDynamicValue(
        ctx => ctx.container.get(Mt5AdminContribution)
    );

    // Register the tree widget
    bind(Mt5AdminTreeWidget).toSelf();
    bind(WidgetFactory).toDynamicValue(ctx => ({
        id: MT5_ADMIN_TREE_WIDGET_ID,
        createWidget: () => ctx.container.getAsync<Mt5AdminTreeWidget>(Mt5AdminTreeWidget)
    }));

    // Register the sidebar ViewContainer
    bind(Mt5AdminViewContainerFactory).toSelf().inSingletonScope();
    bind(WidgetFactory).toService(Mt5AdminViewContainerFactory);
});

```

---

<a id='browser-mt5-admin-tree-widget-tsx'></a>
### 63. `browser/mt5-admin-tree-widget.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { injectable, postConstruct, inject } from '@theia/core/shared/inversify';
import { ReactWidget } from '@theia/core/lib/browser';
import { CommandService } from '@theia/core/lib/common/command';
import { MT5_ADMIN_TREE, AdminTreeNode } from '../common/mt5-admin-tree';
import { API } from './modules/api';

export const MT5_ADMIN_TREE_WIDGET_ID = 'mt5-admin-tree-widget';

@injectable()
export class Mt5AdminTreeWidget extends ReactWidget {

    @inject(CommandService)
    protected readonly commandService: CommandService;

    protected expandedNodes = new Set<string>();
    protected selectedNodeId: string | undefined;
    protected groupsList: any[] = [];

    @postConstruct()
    protected init(): void {
        this.id = MT5_ADMIN_TREE_WIDGET_ID;
        this.title.label = 'MT5 Admin';
        this.title.caption = 'MT5 Administrator';
        this.title.closable = false;
        this.title.iconClass = 'codicon codicon-server';
        this.addClass('mt5-admin-tree-widget');
        this.node.tabIndex = 0;

        // Expand top-level sections by default
        this.expandedNodes.add('groups');
        this.expandedNodes.add('clients-and-accounts');
        this.expandedNodes.add('positions');
        this.expandedNodes.add('routing');
        this.expandedNodes.add('symbols');
        
        this.refreshTree();
        this.update();
    }

    async refreshTree(): Promise<void> {
        try {
            const data = await API.getGroups();
            this.groupsList = data;
            this.update();
        } catch (e) {
            console.error('Failed to load groups list for sidebar tree:', e);
        }
    }

    protected toggleNode(id: string): void {
        if (this.expandedNodes.has(id)) {
            this.expandedNodes.delete(id);
        } else {
            this.expandedNodes.add(id);
        }
        this.update();
    }

    protected selectNode(node: AdminTreeNode): void {
        this.selectedNodeId = node.id;
        this.update();
        
        if (node.id.startsWith('groups:')) {
            // Open the master Groups page and pass the selected path
            this.commandService.executeCommand('mt5-admin:open-view', node.id, 'Groups');
        } else {
            this.commandService.executeCommand('mt5-admin:open-view', node.id, node.label);
        }
    }

    protected buildGroupsSubtree(): AdminTreeNode[] {
        const root: AdminTreeNode[] = [];

        const findOrCreateNode = (parentList: AdminTreeNode[], name: string, fullPath: string, isLeaf: boolean): AdminTreeNode => {
            const id = `groups:${fullPath}`;
            let existing = parentList.find(n => n.id === id);
            if (!existing) {
                existing = {
                    id,
                    label: name,
                    icon: isLeaf ? 'folder' : 'folder-active',
                    children: []
                };
                parentList.push(existing);
            }
            return existing;
        };

        for (const g of this.groupsList) {
            const parts = g.name.split('\\').map(p => p.trim()).filter(Boolean);
            let currentLevel = root;
            let pathAccum = '';
            for (let i = 0; i < parts.length; i++) {
                const part = parts[i];
                pathAccum = pathAccum ? `${pathAccum}\\${part}` : part;
                const isLeaf = i === parts.length - 1;
                const node = findOrCreateNode(currentLevel, part, pathAccum, isLeaf);
                currentLevel = node.children!;
            }
        }

        const cleanChildren = (list: AdminTreeNode[]) => {
            for (const n of list) {
                if (n.children && n.children.length === 0) {
                    delete n.children;
                } else if (n.children) {
                    cleanChildren(n.children);
                }
            }
        };
        cleanChildren(root);
        return root;
    }

    protected renderNode(node: AdminTreeNode, depth: number = 0): React.ReactNode {
        // Dynamically compute child items for the groups parent node
        if (node.id === 'groups') {
            node.children = this.buildGroupsSubtree();
        }

        const hasChildren = node.children && node.children.length > 0;
        const isExpanded = this.expandedNodes.has(node.id);
        const isSelected = this.selectedNodeId === node.id;
        const indent = depth * 16;

        return (
            <React.Fragment key={node.id}>
                <div
                    className={`mt5-admin-tree-row${isSelected ? ' selected' : ''}`}
                    style={{ paddingLeft: `${8 + indent}px` }}
                    onClick={() => {
                        if (hasChildren) {
                            this.toggleNode(node.id);
                        } else {
                            this.selectNode(node);
                        }
                    }}
                    onDoubleClick={() => {
                        this.selectNode(node);
                    }}
                    title={node.label}
                >
                    {/* Expand/collapse arrow */}
                    <span className={`mt5-admin-tree-arrow${hasChildren ? ' visible' : ''}`}>
                        {hasChildren
                            ? (isExpanded
                                ? <i className="codicon codicon-chevron-down" />
                                : <i className="codicon codicon-chevron-right" />)
                            : <span style={{ display: 'inline-block', width: '16px' }} />}
                    </span>
                    {/* Node icon */}
                    {node.icon && (
                        <i className={`codicon codicon-${node.icon} mt5-admin-tree-icon`} />
                    )}
                    {/* Node label */}
                    <span className="mt5-admin-tree-label">{node.label}</span>
                </div>

                {/* Children (collapsed if not expanded) */}
                {hasChildren && isExpanded && (
                    <div className="mt5-admin-tree-children">
                        {node.children!.map(child => this.renderNode(child, depth + 1))}
                    </div>
                )}
            </React.Fragment>
        );
    }

    protected render(): React.ReactNode {
        return (
            <div className="mt5-admin-tree-container">
                <div className="mt5-admin-tree-header">
                    <span className="mt5-admin-tree-header-label">ADMINISTRATOR</span>
                    <button className="adm-icon-btn" style={{ marginLeft: 'auto', marginRight: 8 }} onClick={() => this.refreshTree()} title="Refresh sidebar tree">
                        <i className="codicon codicon-refresh" />
                    </button>
                </div>
                <div className="mt5-admin-tree-body">
                    {MT5_ADMIN_TREE.map(node => this.renderNode(node, 0))}
                </div>
            </div>
        );
    }
}

```

---

<a id='browser-mt5-admin-view-container-ts'></a>
### 63. `browser/mt5-admin-view-container.ts`

```typescript
// @ts-nocheck
import { injectable, inject } from '@theia/core/shared/inversify';
import {
    codicon,
    ViewContainer,
    ViewContainerTitleOptions,
    WidgetFactory,
    WidgetManager
} from '@theia/core/lib/browser';
import { MT5_ADMIN_TREE_WIDGET_ID } from './mt5-admin-tree-widget';

export const MT5_ADMIN_CONTAINER_ID = 'mt5-admin-view-container';
export const MT5_ADMIN_CONTAINER_TITLE_OPTIONS: ViewContainerTitleOptions = {
    label: 'MT5 Admin',
    iconClass: codicon('server'),
    closeable: true
};

@injectable()
export class Mt5AdminViewContainerFactory implements WidgetFactory {

    static ID = MT5_ADMIN_CONTAINER_ID;
    readonly id = Mt5AdminViewContainerFactory.ID;

    @inject(ViewContainer.Factory)
    protected readonly viewContainerFactory: ViewContainer.Factory;

    @inject(WidgetManager)
    protected readonly widgetManager: WidgetManager;

    async createWidget(): Promise<ViewContainer> {
        const viewContainer = this.viewContainerFactory({
            id: MT5_ADMIN_CONTAINER_ID,
            progressLocationId: 'mt5-admin'
        });

        viewContainer.addClass('mt5-admin-view-container');
        viewContainer.setTitleOptions(MT5_ADMIN_CONTAINER_TITLE_OPTIONS);

        // Add the tree widget as the single sub-view
        const treeWidget = await this.widgetManager.getOrCreateWidget(MT5_ADMIN_TREE_WIDGET_ID);
        viewContainer.addWidget(treeWidget, {
            order: 0,
            canHide: false,
            initiallyCollapsed: false,
            weight: 100
        });

        return viewContainer;
    }
}

```

---

<a id='browser-modules-api-ts'></a>
### 63. `browser/modules/api.ts`

```typescript
const BASE_URL = 'http://localhost:8000';
const ADMIN_API_KEY = 'default_admin_api_key_token_change_in_production';

interface RequestOptions {
    method?: string;
    body?: any;
    headers?: Record<string, string>;
}

async function apiRequest<T = any>(endpoint: string, options: RequestOptions = {}): Promise<T> {
    const url = `${BASE_URL}${endpoint}`;
    const headers = {
        'Content-Type': 'application/json',
        'X-Admin-API-Key': ADMIN_API_KEY,
        ...options.headers,
    };
    
    const response = await fetch(url, {
        method: options.method || 'GET',
        headers,
        body: options.body ? JSON.stringify(options.body) : undefined,
    });

    if (!response.ok) {
        const errorText = await response.text();
        let errMsg: any = errorText;
        try {
            const errJson = JSON.parse(errorText);
            errMsg = errJson.detail || errMsg;
            if (typeof errMsg === 'object') {
                if (Array.isArray(errMsg)) {
                    errMsg = errMsg.map(e => `${e.loc ? e.loc.join('.') : 'field'}: ${e.msg || JSON.stringify(e)}`).join(', ');
                } else {
                    errMsg = JSON.stringify(errMsg);
                }
            }
        } catch {
            // keep text
        }
        throw new Error(errMsg || `API error ${response.status}`);
    }

    return response.json();
}

export const API = {
    // Accounts
    async getAccounts() {
        return apiRequest('/admin/accounts');
    },
    async getAccountDetail(login: number) {
        return apiRequest(`/admin/accounts/${login}`);
    },
    async createAccount(data: any) {
        return apiRequest('/admin/accounts', { method: 'POST', body: data });
    },
    async updateAccount(login: number, data: any) {
        return apiRequest(`/admin/accounts/${login}`, { method: 'PUT', body: data });
    },
    async deleteAccount(login: number) {
        return apiRequest(`/admin/accounts/${login}`, { method: 'DELETE' });
    },

    // Positions
    async getPositions() {
        return apiRequest('/admin/positions');
    },

    // Deals
    async getDeals() {
        return apiRequest('/admin/deals');
    },

    // Orders
    async getOrders() {
        return apiRequest('/admin/orders');
    },
    async getOrderHistory() {
        return apiRequest('/admin/orders/history');
    },
    async cancelOrder(ticket: number) {
        return apiRequest(`/admin/orders/${ticket}/cancel`, { method: 'POST' });
    },
    async placeOrder(data: { login: number; symbol: string; volume: number; price_request: number; type: number; price_sl?: number; price_tp?: number; type_filling?: string }) {
        return apiRequest('/admin/trade/order', { method: 'POST', body: data });
    },

    // Symbols
    async getSymbols() {
        return apiRequest('/admin/symbols');
    },
    async getSymbolDetail(symbol: string) {
        return apiRequest(`/admin/symbols/${encodeURIComponent(symbol)}`);
    },
    async createSymbol(data: any) {
        return apiRequest('/admin/symbols', { method: 'POST', body: data });
    },
    async deleteSymbol(symbol: string) {
        return apiRequest(`/admin/symbols/${encodeURIComponent(symbol)}`, { method: 'DELETE' });
    },
    async updateSymbol(symbol: string, data: any) {
        return apiRequest(`/admin/symbols/${encodeURIComponent(symbol)}`, { method: 'PUT', body: data });
    },

    // Groups
    async getGroups() {
        return apiRequest('/admin/groups');
    },
    async getGroupDetail(name: string) {
        return apiRequest(`/admin/groups/${encodeURIComponent(name)}`);
    },
    async createGroup(data: { name: string; max_leverage: number; margin_call: number; margin_stop_out: number; spread_override: number }) {
        return apiRequest('/admin/groups', { method: 'POST', body: data });
    },
    async updateGroup(name: string, data: any) {
        return apiRequest(`/admin/groups/${encodeURIComponent(name)}`, { method: 'PUT', body: data });
    },
    async createGroupSymbolOverride(groupName: string, data: { symbol: string; spread_diff: number; commission_rate: number; margin_rate: number; trade_allowed: boolean }) {
        return apiRequest(`/admin/groups/${encodeURIComponent(groupName)}/symbols`, { method: 'POST', body: data });
    },

    // Routing
    async getRoutingRules() {
        return apiRequest('/admin/routing');
    },
    async createRoutingRule(data: { name: string; priority: number; is_enabled: boolean; match_groups?: string[]; match_symbols?: string[]; match_accounts?: string[]; match_order_types?: string[]; match_volume_min?: number; match_volume_max?: number; action: string; gateway_id?: number; delay_seconds?: number }) {
        return apiRequest('/admin/routing', { method: 'POST', body: data });
    },
    async updateRoutingRule(id: number, data: any) {
        return apiRequest(`/admin/routing/${id}`, { method: 'PUT', body: data });
    },
    async deleteRoutingRule(id: number) {
        return apiRequest(`/admin/routing/${id}`, { method: 'DELETE' });
    },
    async enableRoutingRule(id: number) {
        return apiRequest(`/admin/routing/${id}/enable`, { method: 'POST' });
    },
    async disableRoutingRule(id: number) {
        return apiRequest(`/admin/routing/${id}/disable`, { method: 'POST' });
    },
    async reorderRoutingRules(ids: number[]) {
        return apiRequest('/admin/routing/reorder', { method: 'POST', body: ids });
    },

    // Gateways
    async getGateways() {
        return apiRequest('/admin/gateways');
    },
    async createGateway(data: { name: string; type: string; host?: string; port?: number; username?: string; api_key?: string; is_active?: boolean }) {
        return apiRequest('/admin/gateways', { method: 'POST', body: data });
    },
    async updateGateway(id: number, data: any) {
        return apiRequest(`/admin/gateways/${id}`, { method: 'PUT', body: data });
    },
    async testGateway(id: number) {
        return apiRequest(`/admin/gateways/${id}/test`, { method: 'POST' });
    },

    // Live market quotes (for Market Watch debug panel)
    async getTicks(): Promise<Record<string, { bid: number; ask: number; age: number }>> {
        return apiRequest('/admin/ticks');
    },

    // Risk Management (RMS)
    async getRiskSummary() {
        return apiRequest('/admin/risk/summary');
    },
    async getRiskExposure() {
        return apiRequest('/admin/risk/exposure');
    },
    async getRiskMarginCalls() {
        return apiRequest('/admin/risk/margin-calls');
    }
};

```

---

<a id='browser-modules-clients-clientspage-tsx'></a>
### 63. `browser/modules/clients/ClientsPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

interface Client {
    login: number;
    group_name: string;
    balance: number;
    equity: number;
    margin: number;
    free_margin: number;
    leverage: number;
    status: number; // 0 = Normal, 1 = ReadOnly, 2 = Blocked
    settings_json?: any;
}

const STATUS_MAP: Record<number, string> = {
    0: 'active',
    1: 'readonly',
    2: 'disabled'
};

const STATUS_COLOR: Record<string, string> = {
    active:   'var(--theia-successForeground)',
    disabled: 'var(--theia-errorForeground)',
    readonly: '#f0ad4e',
};

interface Props {
    initialTab?: 'accounts' | 'clients' | 'managers' | 'allocations';
}

export function ClientsPage({ initialTab = 'accounts' }: Props): React.ReactElement {
    const [clients, setClients] = React.useState<Client[]>([]);
    const [selected, setSelected] = React.useState<number | null>(null);
    const [filter, setFilter] = React.useState('');
    const [tab, setTab] = React.useState(initialTab);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Context Menu State
    const [contextMenu, setContextMenu] = React.useState<{ x: number; y: number; login: number | null } | null>(null);

    // Create Modal State
    const [showCreateModal, setShowCreateModal] = React.useState(false);
    const [newAccount, setNewAccount] = React.useState({
        login: '',
        group_name: 'demo_group',
        initial_balance: '10000',
        leverage: '100',
        password: 'password123',
        name: '',
        last_name: '',
        middle_name: '',
        company: '',
        email: '',
        phone: '',
        country: '',
        state: '',
        city: '',
        zip_code: '',
        address: '',
        investor_password: '',
        phone_password: ''
    });
    const [createError, setCreateError] = React.useState<string | null>(null);

    // Edit Modal State
    const [showEditModal, setShowEditModal] = React.useState(false);
    const [editingTab, setEditingTab] = React.useState<'overview' | 'personal' | 'account' | 'limits' | 'security'>('overview');
    const [editingAccount, setEditingAccount] = React.useState<any>(null);
    const [editError, setEditError] = React.useState<string | null>(null);

    const loadAccounts = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getAccounts();
            setClients(data);
        } catch (err: any) {
            setError(err.message || 'Failed to fetch accounts from broker server.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadAccounts();
    }, []);

    React.useEffect(() => {
        const handleOutsideClick = () => setContextMenu(null);
        window.addEventListener('click', handleOutsideClick);
        return () => window.removeEventListener('click', handleOutsideClick);
    }, []);

    const handleCreateAccount = async (e: React.FormEvent) => {
        e.preventDefault();
        setCreateError(null);
        try {
            const payload = {
                group_name: newAccount.group_name,
                initial_balance: parseFloat(newAccount.initial_balance) || 0,
                leverage: parseInt(newAccount.leverage) || 100,
                password: newAccount.password,
                // Extra fields stored in settings_json on create
                name: newAccount.name,
                last_name: newAccount.last_name,
                middle_name: newAccount.middle_name,
                company: newAccount.company,
                email: newAccount.email,
                phone: newAccount.phone,
                country: newAccount.country,
                state: newAccount.state,
                city: newAccount.city,
                zip_code: newAccount.zip_code,
                address: newAccount.address,
                investor_password: newAccount.investor_password,
                phone_password: newAccount.phone_password
            };
            if (newAccount.login && newAccount.login.toLowerCase() !== 'next') {
                payload.login = parseInt(newAccount.login);
            }
            await API.createAccount(payload);
            setShowCreateModal(false);
            setNewAccount({
                login: '',
                group_name: 'demo_group',
                initial_balance: '10000',
                leverage: '100',
                password: 'password123',
                name: '',
                last_name: '',
                middle_name: '',
                company: '',
                email: '',
                phone: '',
                country: '',
                state: '',
                city: '',
                zip_code: '',
                address: '',
                investor_password: '',
                phone_password: ''
            });
            await loadAccounts();
        } catch (err: any) {
            setCreateError(err.message || 'Failed to create account.');
        }
    };

    const handleOpenEdit = (login: number) => {
        const client = clients.find(c => c.login === login);
        if (!client) return;

        // Parse custom settings or set defaults
        const custom = client.settings_json || {};
        setEditingAccount({
            ...client,
            name: custom.name || '',
            last_name: custom.last_name || '',
            middle_name: custom.middle_name || '',
            company: custom.company || '',
            email: custom.email || '',
            phone: custom.phone || '',
            country: custom.country || '',
            state: custom.state || '',
            city: custom.city || '',
            zip_code: custom.zip_code || '',
            address: custom.address || '',
            registered: custom.registered || new Date().toLocaleDateString(),
            language: custom.language || 'English',
            resident_status: custom.resident_status || 'RE',
            id_number: custom.id_number || '',
            lead_source: custom.lead_source || '',
            lead_campaign: custom.lead_campaign || '',
            metaquotes_id: custom.metaquotes_id || '',
            comment: custom.comment || '',

            // Account Tab
            color: custom.color || '#000000',
            bank_account: custom.bank_account || '',
            agent_account: custom.agent_account || '',
            enable_account: custom.enable_account ?? true,
            allow_change_password: custom.allow_change_password ?? true,
            enable_otp: custom.enable_otp ?? false,
            change_pass_next_login: custom.change_pass_next_login ?? false,

            // Limits Tab
            show_to_regular_managers: custom.show_to_regular_managers ?? true,
            include_in_server_reports: custom.include_in_server_reports ?? true,
            enable_daily_reports: custom.enable_daily_reports ?? true,
            enable_sponsored_vps: custom.enable_sponsored_vps ?? false,
            enable_trading: custom.enable_trading ?? true,
            enable_ea: custom.enable_ea ?? true,
            enable_trailing_stops: custom.enable_trailing_stops ?? true,
            limit_position_value: custom.limit_position_value || '',
            limit_active_orders: custom.limit_active_orders || '',

            // Security Passwords State
            master_pass: '',
            investor_pass: '',
            phone_pass: '',
            otp_secret: custom.otp_secret || 'A1B2C3D4E5F6'
        });
        setEditingTab('overview');
        setShowEditModal(true);
    };

    const handleSaveEditAccount = async (e: React.FormEvent) => {
        e.preventDefault();
        setEditError(null);
        try {
            // In a real application, we would call an update API.
            // Let's call the API if it supports PUT /admin/accounts or update locally
            const payload = {
                login: editingAccount.login,
                group_name: editingAccount.group_name,
                leverage: editingAccount.leverage,
                status: editingAccount.enable_account ? 0 : 2, // Map to active/disabled
                settings_json: {
                    ...editingAccount
                }
            };
            
            // Call API update if available, or fallback
            if (API.updateAccount) {
                await API.updateAccount(payload.login, payload);
            } else {
                // Mock local update
                setClients(prev => prev.map(c => c.login === editingAccount.login ? {
                    ...c,
                    group_name: editingAccount.group_name,
                    leverage: editingAccount.leverage,
                    status: editingAccount.enable_account ? 0 : 2,
                    settings_json: editingAccount
                } : c));
            }
            setShowEditModal(false);
            await loadAccounts();
        } catch (err: any) {
            setEditError(err.message || 'Failed to update account.');
        }
    };

    const handleDeleteAccount = async (login: number) => {
        if (!confirm(`Are you sure you want to delete account #${login}?`)) return;
        try {
            await API.deleteAccount(login);
            setSelected(null);
            await loadAccounts();
        } catch (err: any) {
            alert(err.message || 'Failed to delete account.');
        }
    };

    const handleContextMenu = (e: React.MouseEvent, login: number | null) => {
        e.preventDefault();
        setContextMenu({
            x: e.clientX,
            y: e.clientY,
            login
        });
    };

    const filtered = clients.filter(c =>
        String(c.login).includes(filter) ||
        c.group_name.toLowerCase().includes(filter.toLowerCase())
    );

    const selectedClient = clients.find(c => c.login === selected);

    return (
        <div className="adm-page" onContextMenu={e => handleContextMenu(e, null)}>
            <div className="adm-tabs">
                {(['accounts', 'clients', 'managers', 'allocations'] as const).map(t => (
                    <button key={t} className={`adm-tab ${tab === t ? 'active' : ''}`} onClick={() => setTab(t)}>
                        {t === 'accounts' ? 'Trading Accounts' : t.charAt(0).toUpperCase() + t.slice(1)}
                    </button>
                ))}
            </div>

            <div className="adm-toolbar">
                <button className="adm-btn adm-btn-primary" onClick={() => setShowCreateModal(true)}>
                    <i className="codicon codicon-add" /> New Account
                </button>
                {selected !== null && (
                    <>
                        <button className="adm-btn" onClick={() => handleOpenEdit(selected)}>
                            <i className="codicon codicon-edit" /> Edit
                        </button>
                        <button className="adm-btn" onClick={() => handleDeleteAccount(selected)} style={{ color: 'var(--theia-errorForeground)' }}>
                            <i className="codicon codicon-trash" /> Delete
                        </button>
                    </>
                )}
                <button className="adm-btn" onClick={loadAccounts} title="Reload list">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div className="adm-toolbar-sep" />
                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input className="adm-search" placeholder="Search login or group..." value={filter} onChange={e => setFilter(e.target.value)} />
                </div>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-split-view" style={{ flex: 1, minHeight: 0 }}>
                <div className="adm-table-wrap" style={{ flex: selectedClient ? '0 0 60%' : '1', overflowY: 'auto' }}>
                    {loading ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading accounts...</div>
                    ) : filtered.length === 0 ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No accounts found. Use "New Account" to create one.</div>
                    ) : (
                        <table className="adm-table">
                            <thead>
                                <tr>
                                    <th>Login</th>
                                    <th>Group Name</th>
                                    <th>Balance</th>
                                    <th>Equity</th>
                                    <th>Free Margin</th>
                                    <th>Leverage</th>
                                    <th>Status</th>
                                </tr>
                            </thead>
                            <tbody>
                                {filtered.map(c => {
                                    const statusStr = STATUS_MAP[c.status] || 'unknown';
                                    return (
                                        <tr 
                                            key={c.login} 
                                            className={selected === c.login ? 'selected' : ''} 
                                            onClick={() => setSelected(c.login)}
                                            onDoubleClick={() => handleOpenEdit(c.login)}
                                            onContextMenu={e => handleContextMenu(e, c.login)}
                                        >
                                            <td><strong>{c.login}</strong></td>
                                            <td><code className="adm-code">{c.group_name}</code></td>
                                            <td className="adm-num">{c.balance.toLocaleString('en', { minimumFractionDigits: 2 })}</td>
                                            <td className={`adm-num ${c.equity >= c.balance ? 'adm-pos' : 'adm-neg'}`}>{c.equity.toLocaleString('en', { minimumFractionDigits: 2 })}</td>
                                            <td className="adm-num">{c.free_margin.toLocaleString('en', { minimumFractionDigits: 2 })}</td>
                                            <td>1:{c.leverage}</td>
                                            <td><span className="adm-dot" style={{ background: STATUS_COLOR[statusStr] || '#888' }} />{statusStr}</td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    )}
                </div>

                {selectedClient && (
                    <div className="adm-detail-panel" style={{ overflowY: 'auto' }}>
                        <div className="adm-detail-header">
                            <span>Account #{selectedClient.login}</span>
                            <button className="adm-icon-btn" onClick={() => setSelected(null)}><i className="codicon codicon-close" /></button>
                        </div>
                        <div className="adm-detail-body">
                            <div className="adm-detail-section">General Information</div>
                            <div className="adm-kv"><span>Login</span><strong>{selectedClient.login}</strong></div>
                            <div className="adm-kv"><span>Group</span><code className="adm-code">{selectedClient.group_name}</code></div>
                            <div className="adm-kv"><span>Leverage</span><span>1:{selectedClient.leverage}</span></div>
                            
                            <div className="adm-detail-section">Balance & Margins</div>
                            <div className="adm-kv"><span>Balance</span><strong>{(selectedClient.balance ?? 0).toFixed(2)} USD</strong></div>
                            <div className="adm-kv"><span>Equity</span><strong className={(selectedClient.equity ?? 0) >= (selectedClient.balance ?? 0) ? 'adm-pos' : 'adm-neg'}>{(selectedClient.equity ?? 0).toFixed(2)} USD</strong></div>
                            <div className="adm-kv"><span>Margin</span><span>{(selectedClient.margin ?? 0).toFixed(2)} USD</span></div>
                            <div className="adm-kv"><span>Free Margin</span><span>{(selectedClient.free_margin ?? 0).toFixed(2)} USD</span></div>
                            
                            <div className="adm-detail-section">Security & Status</div>
                            <div className="adm-kv"><span>Status</span><span style={{ color: STATUS_COLOR[STATUS_MAP[selectedClient.status]] || '#888' }}>{STATUS_MAP[selectedClient.status] || 'unknown'}</span></div>
                        </div>
                        <div className="adm-detail-footer">
                            <button className="adm-btn adm-btn-primary" onClick={() => handleOpenEdit(selectedClient.login)}>Edit Details</button>
                        </div>
                    </div>
                )}
            </div>

            {/* Context Menu Render */}
            {contextMenu && (
                <div 
                    className="adm-context-menu"
                    style={{
                        position: 'fixed',
                        top: contextMenu.y,
                        left: contextMenu.x,
                        background: 'var(--theia-menu-background, #252526)',
                        border: '1px solid var(--theia-menu-border, #454545)',
                        boxShadow: '0 2px 8px rgba(0,0,0,0.5)',
                        zIndex: 10000,
                        padding: '4px 0',
                        minWidth: 170
                    }}
                    onClick={e => e.stopPropagation()}
                >
                    <div 
                        className="adm-menu-item" 
                        onClick={() => { setShowCreateModal(true); setContextMenu(null); }}
                        style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                    >
                        <i className="codicon codicon-add" /> New Account
                    </div>
                    {contextMenu.login !== null ? (
                        <>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => { handleOpenEdit(contextMenu.login!); setContextMenu(null); }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-edit" /> Edit
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    const c = clients.find(cl => cl.login === contextMenu.login);
                                    if (c) alert(`Open group settings for: ${c.group_name}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-organization" /> Edit Group
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Edit manager profile linked to login ${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-person" /> Edit Manager
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => { handleDeleteAccount(contextMenu.login!); setContextMenu(null); }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', color: 'var(--theia-errorForeground)', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-trash" /> Delete
                            </div>
                            <div style={{ height: 1, background: 'var(--theia-menu-border, #454545)', margin: '4px 0' }} />
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Move account #${contextMenu.login} to archive`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-archive" /> Move to Archive
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Checking balance consistency for account #${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-check" /> Check Balance
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Fixing balance fields for account #${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-tools" /> Fix Balance
                            </div>
                            <div style={{ height: 1, background: 'var(--theia-menu-border, #454545)', margin: '4px 0' }} />
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    navigator.clipboard.writeText(`Login: ${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-copy" /> Copy Lines
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    navigator.clipboard.writeText(String(contextMenu.login));
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-list-unordered" /> Copy Login
                            </div>
                            <div style={{ height: 1, background: 'var(--theia-menu-border, #454545)', margin: '4px 0' }} />
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Exporting trade account #${contextMenu.login} data to CSV/HTML`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-cloud-upload" /> Export Account
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Opening email compose window for: ${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-mail" /> Send E-Mail
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => {
                                    alert(`Loading server journal entries for account #${contextMenu.login}`);
                                    setContextMenu(null);
                                }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-output" /> View Journal
                            </div>
                        </>
                    ) : (
                        <>
                            <div style={{ height: 1, background: 'var(--theia-menu-border, #454545)', margin: '4px 0' }} />
                            <div 
                                className="adm-menu-item" 
                                onClick={() => { loadAccounts(); setContextMenu(null); }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-refresh" /> Request Accounts
                            </div>
                            <div 
                                className="adm-menu-item" 
                                onClick={() => { alert('Import accounts from CSV file'); setContextMenu(null); }}
                                style={{ padding: '6px 12px', fontSize: 11, cursor: 'pointer', display: 'flex', alignItems: 'center', gap: 6 }}
                            >
                                <i className="codicon codicon-cloud-download" /> Import from File
                            </div>
                        </>
                    )}
                </div>
            )}

            {/* CREATE ACCOUNT DIALOG (Boxed layout: Details & Passwords) */}
            {showCreateModal && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setShowCreateModal(false)}>
                    <form 
                        className="adm-modal" 
                        style={{ width: 650, height: '65vh', display: 'flex', flexDirection: 'column' }} 
                        onClick={e => e.stopPropagation()} 
                        onSubmit={handleCreateAccount}
                    >
                        <div className="adm-modal-header" style={{ flexShrink: 0 }}>
                            <h2>Create New Trade Account</h2>
                            <button type="button" className="adm-modal-close" onClick={() => setShowCreateModal(false)}>×</button>
                        </div>
                        <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 16, padding: 16 }}>
                            {createError && (
                                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: 0 }}>
                                    <i className="codicon codicon-error" /> {createError}
                                </div>
                            )}

                            {/* Details Box */}
                            <div style={{ border: '1px solid var(--theia-border)', borderRadius: 4, padding: 12 }}>
                                <h3 style={{ margin: '0 0 12px 0', fontSize: 12, borderBottom: '1px solid var(--theia-border)', paddingBottom: 4 }}>Details</h3>
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Preferred Login</span>
                                        <input className="adm-input" placeholder="Next" value={newAccount.login} onChange={e => setNewAccount({ ...newAccount, login: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Group Name</span>
                                        <input className="adm-input" required placeholder="demo_group" value={newAccount.group_name} onChange={e => setNewAccount({ ...newAccount, group_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Name</span>
                                        <input className="adm-input" required placeholder="First name" value={newAccount.name} onChange={e => setNewAccount({ ...newAccount, name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Last Name</span>
                                        <input className="adm-input" required placeholder="Last name" value={newAccount.last_name} onChange={e => setNewAccount({ ...newAccount, last_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Middle Name</span>
                                        <input className="adm-input" placeholder="Middle name" value={newAccount.middle_name} onChange={e => setNewAccount({ ...newAccount, middle_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Company</span>
                                        <input className="adm-input" placeholder="Company (optional)" value={newAccount.company} onChange={e => setNewAccount({ ...newAccount, company: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>E-Mail</span>
                                        <input className="adm-input" required type="email" placeholder="email@address.com" value={newAccount.email} onChange={e => setNewAccount({ ...newAccount, email: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Phone</span>
                                        <input className="adm-input" required placeholder="+1234567890" value={newAccount.phone} onChange={e => setNewAccount({ ...newAccount, phone: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Country</span>
                                        <input className="adm-input" placeholder="Country" value={newAccount.country} onChange={e => setNewAccount({ ...newAccount, country: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>State</span>
                                        <input className="adm-input" placeholder="State/Region" value={newAccount.state} onChange={e => setNewAccount({ ...newAccount, state: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>City</span>
                                        <input className="adm-input" placeholder="City" value={newAccount.city} onChange={e => setNewAccount({ ...newAccount, city: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Zip Code</span>
                                        <input className="adm-input" placeholder="Zip code" value={newAccount.zip_code} onChange={e => setNewAccount({ ...newAccount, zip_code: e.target.value })} />
                                    </div>
                                </div>
                                <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4, marginTop: 10 }}>
                                    <span style={{ fontSize: 10 }}>Address</span>
                                    <input className="adm-input" placeholder="Street address" value={newAccount.address} onChange={e => setNewAccount({ ...newAccount, address: e.target.value })} />
                                </div>
                            </div>

                            {/* Passwords Box */}
                            <div style={{ border: '1px solid var(--theia-border)', borderRadius: 4, padding: 12 }}>
                                <h3 style={{ margin: '0 0 12px 0', fontSize: 12, borderBottom: '1px solid var(--theia-border)', paddingBottom: 4 }}>Passwords</h3>
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Master Password</span>
                                        <input className="adm-input" required type="password" placeholder="Master password" value={newAccount.password} onChange={e => setNewAccount({ ...newAccount, password: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Investor Password</span>
                                        <input className="adm-input" type="password" placeholder="Investor password" value={newAccount.investor_password} onChange={e => setNewAccount({ ...newAccount, investor_password: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Phone Password</span>
                                        <input className="adm-input" type="password" placeholder="Phone password" value={newAccount.phone_password} onChange={e => setNewAccount({ ...newAccount, phone_password: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Initial Balance (USD)</span>
                                        <input className="adm-input" type="number" required placeholder="10000" value={newAccount.initial_balance} onChange={e => setNewAccount({ ...newAccount, initial_balance: e.target.value })} />
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="adm-modal-footer" style={{ flexShrink: 0 }}>
                            <button type="submit" className="adm-btn adm-btn-primary">Create</button>
                            <button type="button" className="adm-btn" onClick={() => setShowCreateModal(false)}>Cancel</button>
                        </div>
                    </form>
                </div>
            )}

            {/* EDIT ACCOUNT DIALOG (Tabs: Overview, Personal, Account, Limits, Security) */}
            {showEditModal && editingAccount && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setShowEditModal(false)}>
                    <form 
                        className="adm-modal" 
                        style={{ width: 650, height: '65vh', display: 'flex', flexDirection: 'column' }} 
                        onClick={e => e.stopPropagation()} 
                        onSubmit={handleSaveEditAccount}
                    >
                        <div className="adm-modal-header" style={{ flexShrink: 0 }}>
                            <h2>Edit Account - #{editingAccount.login}</h2>
                            <button type="button" className="adm-modal-close" onClick={() => setShowEditModal(false)}>×</button>
                        </div>

                        {/* Dialogue Tab Selector */}
                        <div style={{ display: 'flex', background: 'var(--theia-editor-background)', borderBottom: '1px solid var(--theia-border)', padding: '0 12px', gap: 8, flexShrink: 0 }}>
                            {(['overview', 'personal', 'account', 'limits', 'security'] as const).map((tabId) => (
                                <button
                                    key={tabId}
                                    type="button"
                                    className={`adm-tab ${editingTab === tabId ? 'active' : ''}`}
                                    onClick={() => setEditingTab(tabId)}
                                    style={{
                                        border: 'none',
                                        background: 'transparent',
                                        padding: '8px 12px',
                                        fontSize: 11,
                                        cursor: 'pointer',
                                        textTransform: 'capitalize',
                                        borderBottom: editingTab === tabId ? '2px solid var(--theia-accentColor, #3498db)' : '2px solid transparent',
                                        color: editingTab === tabId ? 'var(--theia-foreground)' : 'var(--theia-descriptionForeground)'
                                    }}
                                >
                                    {tabId}
                                </button>
                            ))}
                        </div>

                        <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', padding: 16 }}>
                            {editError && (
                                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 12px 0' }}>
                                    <i className="codicon codicon-error" /> {editError}
                                </div>
                            )}

                            {/* --- OVERVIEW TAB --- */}
                            {editingTab === 'overview' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 8, background: 'var(--theia-sideBarSectionHeader-background)', padding: 8, borderRadius: 4 }}>
                                        <div style={{ fontSize: 11 }}><strong>Registered:</strong> {editingAccount.registered}</div>
                                        <div style={{ fontSize: 11 }}><strong>Last access:</strong> {editingAccount.registered}</div>
                                        <div style={{ fontSize: 11 }}><strong>Visitor ID:</strong> {editingAccount.login * 3}</div>
                                        <div style={{ fontSize: 11 }}><strong>Affiliate:</strong> Web Portal</div>
                                    </div>

                                    {/* Open Positions Grid */}
                                    <div>
                                        <h4 style={{ margin: '0 0 4px 0', fontSize: 11 }}>Open Positions</h4>
                                        <div style={{ border: '1px solid var(--theia-border)', maxHeight: 100, overflowY: 'auto' }}>
                                            <table className="adm-table" style={{ fontSize: 10 }}>
                                                <thead>
                                                    <tr>
                                                        <th>Symbol</th>
                                                        <th>Ticket</th>
                                                        <th>Type</th>
                                                        <th>Volume</th>
                                                        <th>Price</th>
                                                        <th>Profit</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>EURUSD</td>
                                                        <td>94812</td>
                                                        <td style={{ color: 'var(--theia-successForeground)' }}>Buy</td>
                                                        <td>1.00</td>
                                                        <td>1.09210</td>
                                                        <td className="adm-pos">+120.00</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>

                                    {/* Account State Bar */}
                                    <div style={{ display: 'flex', justifyContent: 'space-between', padding: 8, background: 'var(--theia-sideBar-background)', border: '1px solid var(--theia-border)', fontSize: 11 }}>
                                        <div>Balance: <strong>{editingAccount.balance?.toFixed(2) || '0.00'}</strong></div>
                                        <div>Credit: <strong>0.00</strong></div>
                                        <div>Commission: <strong>0.00</strong></div>
                                        <div>Profit: <strong>+120.00</strong></div>
                                    </div>

                                    {/* Pending Orders Grid */}
                                    <div>
                                        <h4 style={{ margin: '0 0 4px 0', fontSize: 11 }}>Pending Orders</h4>
                                        <div style={{ border: '1px solid var(--theia-border)', maxHeight: 100, overflowY: 'auto' }}>
                                            <table className="adm-table" style={{ fontSize: 10 }}>
                                                <thead>
                                                    <tr>
                                                        <th>Symbol</th>
                                                        <th>Ticket</th>
                                                        <th>Type</th>
                                                        <th>Volume</th>
                                                        <th>Price</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <td>GBPUSD</td>
                                                        <td>94813</td>
                                                        <td>Buy Limit</td>
                                                        <td>0.50</td>
                                                        <td>1.26100</td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            )}

                            {/* --- PERSONAL TAB --- */}
                            {editingTab === 'personal' && (
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 10 }}>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Name</span>
                                        <input className="adm-input" value={editingAccount.name} onChange={e => setEditingAccount({ ...editingAccount, name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Last Name</span>
                                        <input className="adm-input" value={editingAccount.last_name} onChange={e => setEditingAccount({ ...editingAccount, last_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Middle Name</span>
                                        <input className="adm-input" value={editingAccount.middle_name} onChange={e => setEditingAccount({ ...editingAccount, middle_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Company</span>
                                        <input className="adm-input" value={editingAccount.company} onChange={e => setEditingAccount({ ...editingAccount, company: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Language</span>
                                        <input className="adm-input" value={editingAccount.language} onChange={e => setEditingAccount({ ...editingAccount, language: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Status (RE / NR)</span>
                                        <select className="adm-input" value={editingAccount.resident_status} onChange={e => setEditingAccount({ ...editingAccount, resident_status: e.target.value })}>
                                            <option value="RE">Resident (RE)</option>
                                            <option value="NR">Non-Resident (NR)</option>
                                        </select>
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>ID Number</span>
                                        <input className="adm-input" value={editingAccount.id_number} onChange={e => setEditingAccount({ ...editingAccount, id_number: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>MetaQuotes ID</span>
                                        <input className="adm-input" value={editingAccount.metaquotes_id} onChange={e => setEditingAccount({ ...editingAccount, metaquotes_id: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>E-Mail</span>
                                        <input className="adm-input" value={editingAccount.email} onChange={e => setEditingAccount({ ...editingAccount, email: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Phone</span>
                                        <input className="adm-input" value={editingAccount.phone} onChange={e => setEditingAccount({ ...editingAccount, phone: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>Country</span>
                                        <input className="adm-input" value={editingAccount.country} onChange={e => setEditingAccount({ ...editingAccount, country: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <span style={{ fontSize: 10 }}>City</span>
                                        <input className="adm-input" value={editingAccount.city} onChange={e => setEditingAccount({ ...editingAccount, city: e.target.value })} />
                                    </div>
                                </div>
                            )}

                            {/* --- ACCOUNT TAB --- */}
                            {editingTab === 'account' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                    <div className="adm-form-row">
                                        <label>Group</label>
                                        <input className="adm-input" value={editingAccount.group_name} onChange={e => setEditingAccount({ ...editingAccount, group_name: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Leverage</label>
                                        <input className="adm-input" type="number" value={editingAccount.leverage} onChange={e => setEditingAccount({ ...editingAccount, leverage: parseInt(e.target.value) || 100 })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Color</label>
                                        <input className="adm-input" style={{ width: 80, height: 28, padding: 0 }} type="color" value={editingAccount.color} onChange={e => setEditingAccount({ ...editingAccount, color: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Bank Account</label>
                                        <input className="adm-input" value={editingAccount.bank_account} onChange={e => setEditingAccount({ ...editingAccount, bank_account: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Agent Account</label>
                                        <input className="adm-input" value={editingAccount.agent_account} onChange={e => setEditingAccount({ ...editingAccount, agent_account: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row" style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start', gap: 4 }}>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                            <input type="checkbox" checked={editingAccount.enable_account} onChange={e => setEditingAccount({ ...editingAccount, enable_account: e.target.checked })} />
                                            <span>Enable this account</span>
                                        </label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                            <input type="checkbox" checked={editingAccount.allow_change_password} onChange={e => setEditingAccount({ ...editingAccount, allow_change_password: e.target.checked })} />
                                            <span>Allow client to change password</span>
                                        </label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                            <input type="checkbox" checked={editingAccount.enable_otp} onChange={e => setEditingAccount({ ...editingAccount, enable_otp: e.target.checked })} />
                                            <span>Enable one-time password (OTP)</span>
                                        </label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                            <input type="checkbox" checked={editingAccount.change_pass_next_login} onChange={e => setEditingAccount({ ...editingAccount, change_pass_next_login: e.target.checked })} />
                                            <span>Force password change at next login</span>
                                        </label>
                                    </div>
                                </div>
                            )}

                            {/* --- LIMITS TAB --- */}
                            {editingTab === 'limits' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.show_to_regular_managers} onChange={e => setEditingAccount({ ...editingAccount, show_to_regular_managers: e.target.checked })} />
                                        <span>Show to regular managers</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.include_in_server_reports} onChange={e => setEditingAccount({ ...editingAccount, include_in_server_reports: e.target.checked })} />
                                        <span>Include in server reports</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.enable_daily_reports} onChange={e => setEditingAccount({ ...editingAccount, enable_daily_reports: e.target.checked })} />
                                        <span>Enable daily reports</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.enable_sponsored_vps} onChange={e => setEditingAccount({ ...editingAccount, enable_sponsored_vps: e.target.checked })} />
                                        <span>Enable sponsored VPS hosting</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.enable_trading} onChange={e => setEditingAccount({ ...editingAccount, enable_trading: e.target.checked })} />
                                        <span>Enable trading</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.enable_ea} onChange={e => setEditingAccount({ ...editingAccount, enable_ea: e.target.checked })} />
                                        <span>Enable algo trading (Expert Advisors)</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={editingAccount.enable_trailing_stops} onChange={e => setEditingAccount({ ...editingAccount, enable_trailing_stops: e.target.checked })} />
                                        <span>Enable trailing stops</span>
                                    </label>
                                    <div className="adm-form-row" style={{ marginTop: 6 }}>
                                        <label>Limit positions value</label>
                                        <input className="adm-input" placeholder="unlimited" value={editingAccount.limit_position_value} onChange={e => setEditingAccount({ ...editingAccount, limit_position_value: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Limit active orders</label>
                                        <input className="adm-input" placeholder="default" value={editingAccount.limit_active_orders} onChange={e => setEditingAccount({ ...editingAccount, limit_active_orders: e.target.value })} />
                                    </div>
                                </div>
                            )}

                            {/* --- SECURITY TAB --- */}
                            {editingTab === 'security' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                    <div style={{ border: '1px solid var(--theia-border)', padding: 10, borderRadius: 4 }}>
                                        <span style={{ fontSize: 11, fontWeight: 'bold' }}>Master Password</span>
                                        <div style={{ display: 'flex', gap: 6, marginTop: 6 }}>
                                            <input className="adm-input" type="password" placeholder="New master password" value={editingAccount.master_pass} onChange={e => setEditingAccount({ ...editingAccount, master_pass: e.target.value })} />
                                            <button type="button" className="adm-btn" onClick={() => setEditingAccount({ ...editingAccount, master_pass: Math.random().toString(36).slice(-8) + 'A1!' })}>Generate</button>
                                        </div>
                                    </div>
                                    <div style={{ border: '1px solid var(--theia-border)', padding: 10, borderRadius: 4 }}>
                                        <span style={{ fontSize: 11, fontWeight: 'bold' }}>Investor Password</span>
                                        <div style={{ display: 'flex', gap: 6, marginTop: 6 }}>
                                            <input className="adm-input" type="password" placeholder="New investor password" value={editingAccount.investor_pass} onChange={e => setEditingAccount({ ...editingAccount, investor_pass: e.target.value })} />
                                        </div>
                                    </div>
                                    <div style={{ border: '1px solid var(--theia-border)', padding: 10, borderRadius: 4 }}>
                                        <span style={{ fontSize: 11, fontWeight: 'bold' }}>Phone Password</span>
                                        <div style={{ display: 'flex', gap: 6, marginTop: 6 }}>
                                            <input className="adm-input" type="password" placeholder="New phone password" value={editingAccount.phone_pass} onChange={e => setEditingAccount({ ...editingAccount, phone_pass: e.target.value })} />
                                        </div>
                                    </div>
                                    <div className="adm-form-row">
                                        <label>OTP Secret Key</label>
                                        <input className="adm-input" value={editingAccount.otp_secret} onChange={e => setEditingAccount({ ...editingAccount, otp_secret: e.target.value })} />
                                    </div>
                                </div>
                            )}
                        </div>

                        <div className="adm-modal-footer" style={{ flexShrink: 0 }}>
                            <button type="submit" className="adm-btn adm-btn-primary">Save Changes</button>
                            <button type="button" className="adm-btn" onClick={() => setShowEditModal(false)}>Cancel</button>
                        </div>
                    </form>
                </div>
            )}

            <div className="adm-statusbar">
                <span>Accounts: {filtered.length}</span>
                <span className="adm-sep">|</span>
                <span>Active: {filtered.filter(c => c.status === 0).length}</span>
                <span className="adm-sep">|</span>
                <span>ReadOnly/Disabled: {filtered.filter(c => c.status !== 0).length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-data-feeds-datafeedspage-tsx'></a>
### 63. `browser/modules/data-feeds/DataFeedsPage.tsx`

```tsx
import * as React from 'react';
import { API } from '../api';

const STATUS_COLOR: Record<string, string> = {
    connected: 'var(--theia-successForeground)',
    connecting: 'var(--theia-warningForeground, #f1c40f)',
    disconnected: 'var(--theia-descriptionForeground)',
    error: 'var(--theia-errorForeground)',
};

interface FeederModule {
    id: string;
    name: string;
    dll: string;
    description: string;
}

const AVAILABLE_MODULES: FeederModule[] = [
    { id: 'MT5', name: 'MetaTrader 5 Feeder', dll: 'mt5_feeder.dll', description: 'Quotes and news synchronization feed bridge for MT5 clusters.' },
    { id: 'LMAX', name: 'LMAX Global Feeder', dll: 'lmax_feeder.dll', description: 'High-frequency institutional liquidity and price feed connector.' },
    { id: 'Bloomberg', name: 'Bloomberg Feeder', dll: 'bloomberg_feeder.dll', description: 'Financial news and terminal market book provider.' },
    { id: 'IQFeed', name: 'IQFeed Feeder', dll: 'iqfeed_feeder.dll', description: 'Retail market data feed covering forex, futures, and equities.' },
    { id: 'CboeFX', name: 'Cboe FX Feeder', dll: 'cboefx_feeder.dll', description: 'Hotspot / Cboe institutional spot FX market pricing.' },
    { id: 'Currenex', name: 'Currenex Feeder', dll: 'currenex_feeder.dll', description: 'Ecn quotes and trades ingestion adapter.' },
    { id: 'Custom', name: 'Custom Feeder Module', dll: 'custom_feeder.dll', description: 'User-defined custom price source API driver.' }
];

// Helper to build symbol tree from DB list
interface SymbolTreeNode {
    name: string;
    path: string;
    type: 'folder' | 'symbol';
    children: Record<string, SymbolTreeNode>;
}

function buildSymbolTree(symbols: any[]): Record<string, SymbolTreeNode> {
    const root: Record<string, SymbolTreeNode> = {};
    
    symbols.forEach(s => {
        const fullPath = s.symbol || s.name || '';
        if (!fullPath) return;
        const parts = fullPath.split('\\');
        
        let current = root;
        let accumPath = '';
        
        for (let i = 0; i < parts.length; i++) {
            const part = parts[i];
            // skip empty components or dummies
            if (!part || part.startsWith('.')) continue;
            accumPath = accumPath ? `${accumPath}\\${part}` : part;
            const isLast = i === parts.length - 1;
            
            if (!current[part]) {
                current[part] = {
                    name: part,
                    path: accumPath,
                    type: isLast ? 'symbol' : 'folder',
                    children: {}
                };
            }
            current = current[part].children;
        }
    });
    
    return root;
}

interface TreeSelectProps {
    tree: Record<string, SymbolTreeNode>;
    onSelect: (path: string, type: 'folder' | 'symbol') => void;
    depth?: number;
}

function TreeSelect({ tree, onSelect, depth = 0 }: TreeSelectProps) {
    const [expanded, setExpanded] = React.useState<Record<string, boolean>>({
        '*': true,
        'forex': true,
        'crypto': true
    });

    const toggle = (path: string) => {
        setExpanded(prev => ({ ...prev, [path]: !prev[path] }));
    };

    return (
        <div style={{ paddingLeft: depth > 0 ? 12 : 0 }}>
            {Object.values(tree).map((node) => {
                const isFolder = node.type === 'folder';
                const hasChildren = Object.keys(node.children).length > 0;
                const isExpanded = expanded[node.path];

                return (
                    <div key={node.path} style={{ fontSize: 11, userSelect: 'none', fontFamily: 'var(--theia-ui-font-family)' }}>
                        <div 
                            style={{ 
                                display: 'flex', 
                                alignItems: 'center', 
                                gap: 6, 
                                padding: '3px 6px',
                                cursor: 'pointer',
                                borderRadius: 3,
                            }}
                            className="adm-tree-select-row"
                            onClick={(e) => {
                                e.stopPropagation();
                                if (isFolder && hasChildren) {
                                    toggle(node.path);
                                } else {
                                    onSelect(node.path, node.type);
                                }
                            }}
                            onDoubleClick={(e) => {
                                e.stopPropagation();
                                onSelect(node.path, node.type);
                            }}
                        >
                            {/* Expand arrow */}
                            {isFolder ? (
                                <span style={{ width: 10, display: 'inline-flex', justifyContent: 'center', fontSize: 8, opacity: 0.7 }}>
                                    {hasChildren ? (isExpanded ? '▼' : '▶') : ''}
                                </span>
                            ) : (
                                <span style={{ width: 10 }} />
                            )}
                            
                            {/* Icon */}
                            <span style={{ fontSize: 12 }}>
                                {isFolder ? '📁' : '💰'}
                            </span>
                            
                            {/* Label */}
                            <span style={{ 
                                fontWeight: isFolder ? 600 : 'normal',
                                color: isFolder ? 'var(--theia-foreground)' : 'var(--theia-descriptionForeground)'
                            }}>
                                {node.name}
                            </span>

                            {/* Select button for folders */}
                            {isFolder && (
                                <button
                                    type="button"
                                    onClick={(e) => {
                                        e.stopPropagation();
                                        onSelect(node.path === '*' ? '*' : `${node.path}\\*`, 'folder');
                                    }}
                                    style={{
                                        marginLeft: 'auto',
                                        fontSize: 9,
                                        padding: '1px 5px',
                                        background: 'var(--theia-button-background, #34495e)',
                                        color: 'var(--theia-button-foreground, #fff)',
                                        border: 'none',
                                        borderRadius: 2,
                                        cursor: 'pointer'
                                    }}
                                >
                                    Select
                                </button>
                            )}
                        </div>
                        {isFolder && isExpanded && hasChildren && (
                            <TreeSelect tree={node.children} onSelect={onSelect} depth={depth + 1} />
                        )}
                    </div>
                );
            })}
        </div>
    );
}

export function DataFeedsPage(): React.ReactElement {
    const [activeViewTab, setActiveViewTab] = React.useState<'selected' | 'available'>('selected');
    const [feeds, setFeeds] = React.useState<any[]>([]);
    const [selectedFeedId, setSelectedFeedId] = React.useState<number | null>(null);
    const [selectedModuleId, setSelectedModuleId] = React.useState<string | null>(null);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Modal state
    const [showModal, setShowModal] = React.useState(false);
    const [modalMode, setModalMode] = React.useState<'create' | 'edit'>('create');
    const [modalActiveTab, setModalActiveTab] = React.useState<'common' | 'gateway' | 'groups' | 'symbols' | 'translations' | 'parameters'>('common');
    const [modalError, setModalError] = React.useState<string | null>(null);

    // Form fields (Common Tab)
    const [feedForm, setFeedForm] = React.useState({
        id: null as number | null,
        name: '',
        module: 'mt5_feeder.dll',
        host: '',
        port: '',
        username: '',
        api_key: '',
        is_active: true
    });

    // Form fields (Gateway Tab)
    const [gwSettings, setGwSettings] = React.useState({
        gateway_server: '86.104.251.194:443',
        gateway_login: '',
        gateway_password: ''
    });
    const [dbGateways, setDbGateways] = React.useState<any[]>([]);

    // Form fields (Groups Tab)
    const [groupsFilter, setGroupsFilter] = React.useState<string[]>(['*']);
    const [selectedGroupIdx, setSelectedGroupIdx] = React.useState<number | null>(null);
    const [editingGroupIdx, setEditingGroupIdx] = React.useState<number | null>(null);
    const [editingGroupVal, setEditingGroupVal] = React.useState('');

    // Form fields (Symbols Tab)
    const [symbolsFilter, setSymbolsFilter] = React.useState('');

    // Form fields (Translations Tab)
    const [translations, setTranslations] = React.useState<any[]>([]);
    const [newRule, setNewRule] = React.useState({
        symbol: '',
        source: '',
        bid_adj: 0,
        ask_adj: 0
    });

    // Form fields (Parameters Tab)
    const [parameters, setParameters] = React.useState<{ key: string; val: string }[]>([]);
    const [newParam, setNewParam] = React.useState({ key: '', val: '' });

    const lastFeedsRef = React.useRef<any[]>([]);
    const [tickRates, setTickRates] = React.useState<Record<number, number>>({});

    // Symbols tab custom nested tree editor states
    const [dbSymbols, setDbSymbols] = React.useState<any[]>([]);
    const [availableGroups, setAvailableGroups] = React.useState<any[]>([]);
    const [editingIndex, setEditingIndex] = React.useState<number | null>(null);
    const [editValue, setEditValue] = React.useState<string>('');
    const [showTreeIndex, setShowTreeIndex] = React.useState<number | null>(null);
    const [selectedRuleIndex, setSelectedRuleIndex] = React.useState<number | null>(null);
    const [allowImport, setAllowImport] = React.useState<boolean>(false);

    const symbolTree: Record<string, SymbolTreeNode> = React.useMemo(() => {
        const rawTree = buildSymbolTree(dbSymbols);
        return {
            'Symbols': {
                name: 'Symbols',
                path: '*',
                type: 'folder' as 'folder',
                children: rawTree
            }
        };
    }, [dbSymbols]);

    const loadDbSymbols = async () => {
        try {
            const data = await API.getSymbols();
            setDbSymbols(data);
        } catch (e) {
            console.error('Failed to load symbols for data feeds tree view:', e);
        }
    };

    const loadDbGroups = async () => {
        try {
            const data = await API.getGroups();
            setAvailableGroups(data);
        } catch (e) {
            console.error('Failed to load groups for feed settings dropdown:', e);
        }
    };

    const loadFeeds = async (isPoll = false) => {
        if (!isPoll) setLoading(true);
        setError(null);
        try {
            const data = await API.getGateways();
            const filtered = data.filter((g: any) => g.type.startsWith('Feeder_'));
            const tradeGws = data.filter((g: any) => !g.type.startsWith('Feeder_'));
            setDbGateways(tradeGws);
            
            // Calculate tick rates
            const newRates: Record<number, number> = {};
            filtered.forEach((f: any) => {
                const old = lastFeedsRef.current.find(o => o.id === f.id);
                if (old) {
                    const diffTicks = Math.max(0, (f.ticks_count || 0) - (old.ticks_count || 0));
                    newRates[f.id] = diffTicks / 2.0; // Polled every 2 seconds
                } else {
                    newRates[f.id] = 0;
                }
            });
            setTickRates(prev => ({ ...prev, ...newRates }));
            lastFeedsRef.current = filtered;
            setFeeds(filtered);
        } catch (err: any) {
            setError(err.message || 'Failed to load data feeds.');
        } finally {
            if (!isPoll) setLoading(false);
        }
    };

    React.useEffect(() => {
        loadFeeds(false);
        loadDbSymbols();
        loadDbGroups();
        let interval: any = null;
        if (activeViewTab === 'selected') {
            interval = setInterval(() => loadFeeds(true), 2000);
        }
        return () => {
            if (interval) clearInterval(interval);
        };
    }, [activeViewTab]);

    const openCreateModal = (mod: FeederModule) => {
        setModalMode('create');
        setModalActiveTab('common');
        setModalError(null);
        
        setFeedForm({
            id: null,
            name: mod.name + ' 1',
            module: mod.dll,
            host: 'localhost',
            port: '8005',
            username: '',
            api_key: '',
            is_active: true
        });

        setGwSettings({
            gateway_server: '86.104.251.194:443',
            gateway_login: '',
            gateway_password: ''
        });

        setGroupsFilter(['*']);
        setSelectedGroupIdx(null);
        setEditingGroupIdx(null);
        setEditingGroupVal('');

        setSymbolsFilter('Forex*,!Forex\\EURUSD');
        setTranslations([]);
        
        // Reset symbols filter rules edit states
        setEditingIndex(null);
        setSelectedRuleIndex(null);
        setShowTreeIndex(null);
        setAllowImport(false);

        setParameters([
            { key: 'NewsCategory', val: 'General' },
            { key: 'Quotes Delay', val: '0' },
            { key: 'Quotes Ticks Sample', val: '1000' },
            { key: 'Quotes Books Sample', val: '1000' }
        ]);

        setShowModal(true);
    };

    const openEditModal = (f: any) => {
        setModalMode('edit');
        setModalActiveTab('common');
        setModalError(null);

        // Parse feeder type back to dll
        const dllName = f.type.replace('Feeder_', '');

        setFeedForm({
            id: f.id,
            name: f.name,
            module: dllName,
            host: f.host || '',
            port: f.port ? String(f.port) : '',
            username: f.username || '',
            api_key: f.api_key || '',
            is_active: f.is_active === 1
        });

        // Parse settings json
        let gateway = { gateway_server: '86.104.251.194:443', gateway_login: '', gateway_password: '' };
        let groups = ['*'];
        let symFilter = '';
        let rules = [];
        let params: { key: string; val: string }[] = [];

        if (f.settings_json) {
            try {
                const parsed = typeof f.settings_json === 'string' ? JSON.parse(f.settings_json) : f.settings_json;
                if (parsed.gateway) gateway = { ...gateway, ...parsed.gateway };
                if (parsed.groups) groups = parsed.groups;
                if (parsed.symbols_filter) symFilter = parsed.symbols_filter;
                if (parsed.translations) rules = parsed.translations;
                if (parsed.parameters) {
                    params = Object.entries(parsed.parameters).map(([k, v]) => ({ key: k, val: String(v) }));
                }
            } catch (err) {
                // ignore
            }
        }

        // Fill default params if missing
        if (params.length === 0) {
            params = [
                { key: 'NewsCategory', val: 'General' },
                { key: 'Quotes Delay', val: '0' },
                { key: 'Quotes Ticks Sample', val: '1000' },
                { key: 'Quotes Books Sample', val: '1000' }
            ];
        }

        setGwSettings(gateway);
        setGroupsFilter(groups);
        setSelectedGroupIdx(null);
        setEditingGroupIdx(null);
        setEditingGroupVal('');

        setSymbolsFilter(symFilter);
        setTranslations(rules);
        setParameters(params);

        // Reset symbols filter rules edit states
        setEditingIndex(null);
        setSelectedRuleIndex(null);
        setShowTreeIndex(null);
        setAllowImport(false);

        setShowModal(true);
    };
    const filterRules = React.useMemo(() => {
        return symbolsFilter.split(',').map(s => s.trim()).filter(Boolean);
    }, [symbolsFilter]);

    const handleAddFilterRule = () => {
        const newRules = [...filterRules, '*'];
        setSymbolsFilter(newRules.join(','));
        setSelectedRuleIndex(newRules.length - 1);
        setEditingIndex(newRules.length - 1);
        setEditValue('*');
    };

    const handleEditFilterRule = (idx: number) => {
        setEditingIndex(idx);
        setEditValue(filterRules[idx] || '');
        setSelectedRuleIndex(idx);
    };

    const handleDeleteFilterRule = (idx: number) => {
        const newRules = filterRules.filter((_, i) => i !== idx);
        setSymbolsFilter(newRules.join(','));
        setEditingIndex(null);
        setSelectedRuleIndex(null);
        setShowTreeIndex(null);
    };

    const handleSaveFilterRule = (idx: number, val: string) => {
        const newRules = [...filterRules];
        newRules[idx] = val.trim();
        setSymbolsFilter(newRules.filter(Boolean).join(','));
        setEditingIndex(null);
        setShowTreeIndex(null);
    };
    const handleAddRule = () => {
        if (!newRule.symbol.trim() || !newRule.source.trim()) {
            alert('Symbol and Source pattern are required.');
            return;
        }
        setTranslations([...translations, {
            symbol: newRule.symbol.trim(),
            source: newRule.source.trim(),
            bid_adj: Number(newRule.bid_adj) || 0,
            ask_adj: Number(newRule.ask_adj) || 0
        }]);
        setNewRule({ symbol: '', source: '', bid_adj: 0, ask_adj: 0 });
    };

    const handleRemoveRule = (idx: number) => {
        setTranslations(translations.filter((_, i) => i !== idx));
    };

    const handleAddParam = () => {
        if (!newParam.key.trim()) return;
        setParameters([...parameters, { key: newParam.key.trim(), val: newParam.val.trim() }]);
        setNewParam({ key: '', val: '' });
    };

    const handleRemoveParam = (idx: number) => {
        setParameters(parameters.filter((_, i) => i !== idx));
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setModalError(null);

        // Construct settings_json
        const paramObj = parameters.reduce((acc: any, curr) => {
            if (curr.key.trim()) acc[curr.key.trim()] = curr.val;
            return acc;
        }, {});

        const settings = {
            gateway: gwSettings,
            groups: groupsFilter,
            symbols_filter: symbolsFilter,
            translations,
            parameters: paramObj
        };

        const payload = {
            name: feedForm.name,
            type: 'Feeder_' + feedForm.module,
            host: feedForm.host || undefined,
            port: feedForm.port ? parseInt(feedForm.port) : undefined,
            username: feedForm.username || undefined,
            api_key: feedForm.api_key || undefined,
            is_active: feedForm.is_active,
            settings_json: JSON.stringify(settings)
        };

        try {
            if (modalMode === 'create') {
                await API.createGateway(payload);
            } else {
                await API.updateGateway(feedForm.id!, payload);
            }
            setShowModal(false);
            setActiveViewTab('selected');
            await loadFeeds();
        } catch (err: any) {
            setModalError(err.message || 'Failed to save data feed.');
        }
    };

    const handleTestFeed = async () => {
        if (!selectedFeedId) return;
        setError(null);
        try {
            const resp = await API.testGateway(selectedFeedId);
            alert(`Feeder Connection Test: ${resp.message}`);
        } catch (err: any) {
            setError(err.message || 'Feeder connection test failed.');
        }
    };

    const selectedFeed = feeds.find(f => f.id === selectedFeedId);
    const selectedModule = AVAILABLE_MODULES.find(m => m.id === selectedModuleId);

    return (
        <div className="adm-page">
            {/* View Tab Switcher */}
            <div className="adm-tabs" style={{ background: 'var(--theia-editor-background)', borderBottom: '1px solid var(--theia-border)', flexShrink: 0 }}>
                <button className={`adm-tab ${activeViewTab === 'selected' ? 'active' : ''}`} onClick={() => setActiveViewTab('selected')}>
                    Selected Feeds
                </button>
                <button className={`adm-tab ${activeViewTab === 'available' ? 'active' : ''}`} onClick={() => setActiveViewTab('available')}>
                    Available Connectors
                </button>
            </div>

            <div className="adm-toolbar">
                {activeViewTab === 'selected' ? (
                    <>
                        <button className="adm-btn" disabled={!selectedFeedId} onClick={() => selectedFeed && openEditModal(selectedFeed)}>
                            <i className="codicon codicon-edit" /> Edit Feed
                        </button>
                        <button className="adm-btn" disabled={!selectedFeedId} onClick={handleTestFeed}>
                            <i className="codicon codicon-beaker" /> Test Connection
                        </button>
                        <button className="adm-btn" onClick={() => loadFeeds(false)} title="Reload list">
                            <i className="codicon codicon-refresh" /> Refresh
                        </button>
                    </>
                ) : (
                    <button className="adm-btn adm-btn-primary" disabled={!selectedModuleId} onClick={() => selectedModule && openCreateModal(selectedModule)}>
                        <i className="codicon codicon-add" /> Configure Feed...
                    </button>
                )}
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {activeViewTab === 'selected' ? (
                    loading ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading feeders...</div>
                    ) : feeds.length === 0 ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No configured price feeders found. Go to the "Available Connectors" tab to setup a price feed source.</div>
                    ) : (
                        <table className="adm-table">
                            <thead>
                                <tr>
                                    <th></th>
                                    <th>Feed Name</th>
                                    <th>Feeder Module</th>
                                    <th>Server Address</th>
                                    <th>Login ID</th>
                                    <th>Ticks/sec</th>
                                    <th>Status</th>
                                    <th>Last Tick</th>
                                </tr>
                            </thead>
                            <tbody>
                                {feeds.map(f => {
                                    const dll = f.type.replace('Feeder_', '');
                                    const hasTicks = (f.ticks_count || 0) > 0;
                                    const tickAgeSec: number | null = f.last_tick_age_s != null ? f.last_tick_age_s : null;
                                    // Consider disconnected if last tick was > 45 seconds ago
                                    const isTickFresh = tickAgeSec !== null && tickAgeSec < 45;
                                    
                                    let statusStr = 'disconnected';
                                    let dotClass = 'offline';
                                    let dotStyle: React.CSSProperties = {};
                                    
                                    if (f.is_active) {
                                        if (hasTicks && isTickFresh) {
                                            statusStr = 'connected';
                                            dotClass = 'online';
                                        } else if (hasTicks && !isTickFresh) {
                                            // Was connected but ticks stopped - truly disconnected
                                            statusStr = 'disconnected';
                                            dotClass = 'offline';
                                        } else {
                                            statusStr = 'connecting';
                                            dotClass = '';
                                            dotStyle = {
                                                backgroundColor: 'var(--theia-warningForeground, #f1c40f)',
                                                boxShadow: '0 0 4px #f1c40f88'
                                            };
                                        }
                                    }
                                    
                                    const rate = tickRates[f.id] || 0;
                                    const ticksText = f.is_active ? (hasTicks ? `${rate.toFixed(1)} /s (${f.ticks_count} total)` : '0.0 /s') : '—';
                                    
                                    let lastTickText = '—';
                                    if (f.last_active) {
                                        try {
                                            const date = new Date(f.last_active);
                                            lastTickText = date.toLocaleTimeString();
                                            if (tickAgeSec !== null && tickAgeSec > 60) {
                                                lastTickText += ` (${Math.round(tickAgeSec)}s ago)`;
                                            }
                                        } catch (e) {
                                            lastTickText = '—';
                                        }
                                    }

                                    return (
                                        <tr key={f.id} className={selectedFeedId === f.id ? 'selected' : ''} onClick={() => setSelectedFeedId(f.id)} onDoubleClick={() => openEditModal(f)}>
                                            <td><span className={`adm-status-dot ${dotClass}`} style={dotStyle} /></td>
                                            <td><strong>{f.name}</strong></td>
                                            <td><code className="adm-code">{dll}</code></td>
                                            <td>{f.host ? `${f.host}:${f.port || '80'}` : '—'}</td>
                                            <td>{f.username || '—'}</td>
                                            <td className="adm-num">{ticksText}</td>
                                            <td style={{ color: STATUS_COLOR[statusStr] }}>{statusStr}</td>
                                            <td>{lastTickText}</td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    )
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th>Connector Name</th>
                                <th>Feeder Module DLL</th>
                                <th>Description</th>
                            </tr>
                        </thead>
                        <tbody>
                            {AVAILABLE_MODULES.map(m => (
                                <tr key={m.id} className={selectedModuleId === m.id ? 'selected' : ''} onClick={() => setSelectedModuleId(m.id)} onDoubleClick={() => openCreateModal(m)}>
                                    <td><strong>{m.name}</strong></td>
                                    <td><code className="adm-code">{m.dll}</code></td>
                                    <td style={{ opacity: 0.8 }}>{m.description}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>

            {showModal && (
                <div className="adm-modal-overlay" onClick={() => setShowModal(false)}>
                    <form className="adm-modal" style={{ width: 750, height: '65vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }} onClick={e => e.stopPropagation()} onSubmit={handleSubmit}>
                        <div className="adm-modal-header">
                            <h2>{modalMode === 'create' ? `Configure New Feed: ${feedForm.module}` : `Edit Feed settings: ${feedForm.name}`}</h2>
                            <button type="button" className="adm-modal-close" onClick={() => setShowModal(false)}>×</button>
                        </div>

                        {/* Modal Tab Switcher */}
                        <div className="adm-tabs" style={{ padding: '0 16px', borderBottom: '1px solid var(--theia-border)', flexShrink: 0 }}>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'common' ? 'active' : ''}`} onClick={() => setModalActiveTab('common')}>Common</button>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'gateway' ? 'active' : ''}`} onClick={() => setModalActiveTab('gateway')}>Gateway</button>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'groups' ? 'active' : ''}`} onClick={() => setModalActiveTab('groups')}>Groups</button>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'symbols' ? 'active' : ''}`} onClick={() => setModalActiveTab('symbols')}>Symbols</button>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'translations' ? 'active' : ''}`} onClick={() => setModalActiveTab('translations')}>Translations</button>
                            <button type="button" className={`adm-tab ${modalActiveTab === 'parameters' ? 'active' : ''}`} onClick={() => setModalActiveTab('parameters')}>Parameters</button>
                        </div>

                        <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', padding: 16 }}>
                            {modalError && (
                                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 12px 0' }}>
                                    <i className="codicon codicon-error" /> {modalError}
                                </div>
                            )}

                            {modalActiveTab === 'common' && (
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                        <div className="adm-form-row">
                                            <label>Feed Name</label>
                                            <input className="adm-input" required placeholder="e.g. My-LMAX-Feeder" value={feedForm.name} onChange={e => setFeedForm({ ...feedForm, name: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Module DLL</label>
                                            <input className="adm-input" disabled value={feedForm.module} />
                                        </div>
                                        <div className="adm-form-row" style={{ marginTop: 12, flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                                            <input type="checkbox" id="feed_enabled" checked={feedForm.is_active} onChange={e => setFeedForm({ ...feedForm, is_active: e.target.checked })} />
                                            <label htmlFor="feed_enabled" style={{ cursor: 'pointer', margin: 0 }}>Enable Data Feed</label>
                                        </div>
                                    </div>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                        <div className="adm-form-row">
                                            <label>Feed Server Host</label>
                                            <input className="adm-input" required placeholder="e.g. feed.lmax.com" value={feedForm.host} onChange={e => setFeedForm({ ...feedForm, host: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Port</label>
                                            <input className="adm-input" type="number" required placeholder="e.g. 443" value={feedForm.port} onChange={e => setFeedForm({ ...feedForm, port: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Feed Login</label>
                                            <input className="adm-input" placeholder="Login ID" value={feedForm.username} onChange={e => setFeedForm({ ...feedForm, username: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Password / Token</label>
                                            <input className="adm-input" type="password" placeholder="API access password" value={feedForm.api_key} onChange={e => setFeedForm({ ...feedForm, api_key: e.target.value })} />
                                        </div>
                                    </div>
                                </div>
                            )}

                            {modalActiveTab === 'gateway' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12, maxWidth: 400 }}>
                                    <div className="adm-hint" style={{ marginBottom: 10 }}>
                                        <i className="codicon codicon-info" /> Define loopback interface routing servers settings for secure history/trading component tunnels.
                                    </div>
                                    <div className="adm-form-row">
                                        <label style={{ color: 'var(--theia-successForeground)', fontWeight: 'bold' }}>Link with Trade Gateway Profile</label>
                                        <select 
                                            className="adm-select" 
                                            style={{ width: '100%', height: 22, padding: '2px 6px', fontSize: 11 }} 
                                            value=""
                                            onChange={e => {
                                                const chosenId = e.target.value;
                                                if (chosenId) {
                                                    const match = dbGateways.find(g => String(g.id) === chosenId);
                                                    if (match) {
                                                        setGwSettings({
                                                            gateway_server: `${match.host || 'localhost'}:${match.port || '8003'}`,
                                                            gateway_login: match.username || '',
                                                            gateway_password: match.api_key || ''
                                                        });
                                                    }
                                                }
                                            }}
                                        >
                                            <option value="">-- Choose Profile to Auto-Fill Server Details --</option>
                                            {dbGateways.map(g => (
                                                <option key={g.id} value={g.id}>{g.name} ({g.type})</option>
                                            ))}
                                        </select>
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Gateway Server (IP:Port)</label>
                                        <input className="adm-input" value={gwSettings.gateway_server} onChange={e => setGwSettings({ ...gwSettings, gateway_server: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Gateway Login</label>
                                        <input className="adm-input" placeholder="Numeric Login" value={gwSettings.gateway_login} onChange={e => setGwSettings({ ...gwSettings, gateway_login: e.target.value })} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Gateway Password</label>
                                        <input className="adm-input" type="password" placeholder="Loopback key" value={gwSettings.gateway_password} onChange={e => setGwSettings({ ...gwSettings, gateway_password: e.target.value })} />
                                    </div>
                                </div>
                            )}

                            {modalActiveTab === 'groups' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div className="adm-hint" style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)' }}>
                                        Please specify the client groups whose trade operations shall be routed to the liquidity provider through this feed.
                                    </div>
                                    <div style={{ display: 'flex', gap: 16, height: 260 }}>
                                        {/* Action Buttons on Left */}
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, width: 90, flexShrink: 0 }}>
                                            <button 
                                                type="button" 
                                                className="adm-btn" 
                                                onClick={() => {
                                                    const nextIdx = groupsFilter.length;
                                                    setGroupsFilter([...groupsFilter, 'new_group\\*']);
                                                    setSelectedGroupIdx(nextIdx);
                                                    setEditingGroupIdx(nextIdx);
                                                    setEditingGroupVal('new_group\\*');
                                                }}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Add
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn" 
                                                disabled={selectedGroupIdx === null}
                                                onClick={() => {
                                                    if (selectedGroupIdx !== null) {
                                                        setEditingGroupIdx(selectedGroupIdx);
                                                        setEditingGroupVal(groupsFilter[selectedGroupIdx]);
                                                    }
                                                }}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Edit
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn adm-btn-danger" 
                                                disabled={selectedGroupIdx === null}
                                                onClick={() => {
                                                    if (selectedGroupIdx !== null) {
                                                        const updated = groupsFilter.filter((_, idx) => idx !== selectedGroupIdx);
                                                        setGroupsFilter(updated);
                                                        setSelectedGroupIdx(null);
                                                        setEditingGroupIdx(null);
                                                    }
                                                }}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Delete
                                            </button>
                                        </div>

                                        {/* List Box on Right */}
                                        <div style={{ 
                                            flex: 1, 
                                            border: '1px solid var(--theia-input-border, #ccc)', 
                                            background: 'var(--theia-input-background, #fff)', 
                                            color: 'var(--theia-input-foreground, #333)',
                                            borderRadius: 3,
                                            height: '100%',
                                            overflowY: 'auto',
                                            display: 'flex',
                                            flexDirection: 'column'
                                        }}>
                                            {groupsFilter.map((gStr, idx) => {
                                                const isSelected = selectedGroupIdx === idx;
                                                const isEditing = editingGroupIdx === idx;

                                                if (isEditing) {
                                                    return (
                                                        <div key={idx} style={{ padding: '4px 8px', borderBottom: '1px solid var(--theia-panel-border, #eee)', display: 'flex', gap: 8, alignItems: 'center' }}>
                                                            <input 
                                                                className="adm-input" 
                                                                style={{ flex: 1, height: 20, fontSize: 11 }}
                                                                value={editingGroupVal}
                                                                autoFocus
                                                                onChange={e => setEditingGroupVal(e.target.value)}
                                                                placeholder="e.g. real\*"
                                                                onKeyDown={e => {
                                                                    if (e.key === 'Enter') {
                                                                        const updated = [...groupsFilter];
                                                                        updated[idx] = editingGroupVal.trim() || '*';
                                                                        setGroupsFilter(updated);
                                                                        setEditingGroupIdx(null);
                                                                    } else if (e.key === 'Escape') {
                                                                        setEditingGroupIdx(null);
                                                                    }
                                                                }}
                                                            />
                                                            <select
                                                                className="adm-select"
                                                                style={{ width: 180, height: 20, fontSize: 11 }}
                                                                value=""
                                                                onChange={e => {
                                                                    const chosen = e.target.value;
                                                                    if (chosen) {
                                                                        setEditingGroupVal(chosen);
                                                                        const updated = [...groupsFilter];
                                                                        updated[idx] = chosen;
                                                                        setGroupsFilter(updated);
                                                                        setEditingGroupIdx(null);
                                                                    }
                                                                }}
                                                            >
                                                                <option value="">-- Select group... --</option>
                                                                <option value="*">* (All Groups)</option>
                                                                {availableGroups.map(g => (
                                                                    <option key={g.name} value={g.name}>{g.name}</option>
                                                                ))}
                                                            </select>
                                                            <button 
                                                                type="button"
                                                                className="adm-btn adm-btn-primary"
                                                                style={{ height: 20, padding: '0 8px', fontSize: 10, minWidth: 40 }}
                                                                onClick={() => {
                                                                    const updated = [...groupsFilter];
                                                                    updated[idx] = editingGroupVal.trim() || '*';
                                                                    setGroupsFilter(updated);
                                                                    setEditingGroupIdx(null);
                                                                }}
                                                            >
                                                                Save
                                                            </button>
                                                        </div>
                                                    );
                                                }

                                                return (
                                                    <div 
                                                        key={idx}
                                                        style={{ 
                                                            display: 'flex', 
                                                            alignItems: 'center', 
                                                            gap: 8, 
                                                            padding: '6px 12px', 
                                                            cursor: 'default',
                                                            fontSize: 11,
                                                            borderBottom: '1px solid var(--theia-panel-border, #eee)',
                                                            background: isSelected ? 'var(--theia-list-activeSelectionBackground, #3498db)' : 'transparent',
                                                            color: isSelected ? 'var(--theia-list-activeSelectionForeground, #fff)' : 'inherit'
                                                        }}
                                                        onClick={() => setSelectedGroupIdx(idx)}
                                                        onDoubleClick={() => {
                                                            setSelectedGroupIdx(idx);
                                                            setEditingGroupIdx(idx);
                                                            setEditingGroupVal(gStr);
                                                        }}
                                                    >
                                                        <i className="codicon codicon-organization" style={{ color: isSelected ? 'inherit' : '#3498db' }} />
                                                        <strong>{gStr}</strong>
                                                    </div>
                                                );
                                            })}

                                            <div 
                                                style={{ 
                                                    display: 'flex', 
                                                    alignItems: 'center', 
                                                    gap: 8, 
                                                    padding: '6px 12px', 
                                                    cursor: 'pointer',
                                                    fontSize: 11,
                                                    color: 'var(--theia-successForeground)'
                                                }}
                                                onClick={() => {
                                                    const nextIdx = groupsFilter.length;
                                                    setGroupsFilter([...groupsFilter, '']);
                                                    setSelectedGroupIdx(nextIdx);
                                                    setEditingGroupIdx(nextIdx);
                                                    setEditingGroupVal('');
                                                }}
                                            >
                                                <i className="codicon codicon-add" />
                                                <span>click to add...</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            )}

                            {modalActiveTab === 'symbols' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div className="adm-hint" style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)' }}>
                                        Please specify the symbols for which the data feed will translate quotes.
                                    </div>
                                    <div style={{ display: 'flex', gap: 16, height: 260 }}>
                                        {/* Action Buttons on Left */}
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, width: 90, flexShrink: 0 }}>
                                            <button 
                                                type="button" 
                                                className="adm-btn" 
                                                onClick={handleAddFilterRule}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Add
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn" 
                                                disabled={selectedRuleIndex === null}
                                                onClick={() => selectedRuleIndex !== null && handleEditFilterRule(selectedRuleIndex)}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Edit
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn" 
                                                disabled={selectedRuleIndex === null}
                                                onClick={() => selectedRuleIndex !== null && handleDeleteFilterRule(selectedRuleIndex)}
                                                style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                                            >
                                                Delete
                                            </button>
                                        </div>

                                        {/* List Box on Right */}
                                        <div style={{ 
                                            flex: 1, 
                                            border: '1px solid var(--theia-input-border, #ccc)', 
                                            background: 'var(--theia-input-background, #fff)', 
                                            color: 'var(--theia-input-foreground, #333)',
                                            borderRadius: 3,
                                            height: '100%',
                                            overflowY: 'auto',
                                            position: 'relative'
                                        }}>
                                            {filterRules.map((rule, idx) => {
                                                const isSelected = selectedRuleIndex === idx;
                                                const isEditing = editingIndex === idx;
                                                const showTree = showTreeIndex === idx;

                                                return (
                                                    <div 
                                                        key={idx} 
                                                        style={{ 
                                                            display: 'flex', 
                                                            alignItems: 'center', 
                                                            padding: '4px 8px',
                                                            background: isSelected && !isEditing ? 'var(--theia-list-activeSelectionBackground, #3498db)' : 'transparent',
                                                            color: isSelected && !isEditing ? 'var(--theia-list-activeSelectionForeground, #fff)' : 'inherit',
                                                            cursor: 'default',
                                                            borderBottom: '1px solid var(--theia-panel-border, #eee)',
                                                            fontSize: 12,
                                                            position: 'relative'
                                                        }}
                                                        onClick={() => {
                                                            if (!isEditing) {
                                                                setSelectedRuleIndex(idx);
                                                            }
                                                        }}
                                                        onDoubleClick={() => {
                                                            handleEditFilterRule(idx);
                                                        }}
                                                    >
                                                        {/* Symbol Icon */}
                                                        <span style={{ marginRight: 8, display: 'inline-flex', alignItems: 'center' }}>
                                                            {/* Custom premium document with $ sign icon */}
                                                            <span style={{
                                                                display: 'inline-block',
                                                                background: '#f1c40f',
                                                                color: '#2980b9',
                                                                fontSize: 9,
                                                                fontWeight: 'bold',
                                                                padding: '1px 3px',
                                                                borderRadius: 2,
                                                                border: '1px solid #d35400',
                                                                lineHeight: 1
                                                            }}>$</span>
                                                        </span>

                                                        {isEditing ? (
                                                            <div style={{ display: 'flex', flex: 1, gap: 4, alignItems: 'center', position: 'relative' }}>
                                                                <input 
                                                                    className="adm-input" 
                                                                    value={editValue} 
                                                                    onChange={e => setEditValue(e.target.value)}
                                                                    onBlur={(e) => {
                                                                        // Wait, if they clicked on the tree popup, don't save immediately
                                                                        if (e.relatedTarget && (e.relatedTarget as HTMLElement).closest('.adm-tree-popup')) {
                                                                            return;
                                                                        }
                                                                        handleSaveFilterRule(idx, editValue);
                                                                    }}
                                                                    onKeyDown={e => {
                                                                        if (e.key === 'Enter') {
                                                                            handleSaveFilterRule(idx, editValue);
                                                                        } else if (e.key === 'Escape') {
                                                                            setEditingIndex(null);
                                                                            setShowTreeIndex(null);
                                                                        }
                                                                    }}
                                                                    autoFocus
                                                                    style={{ 
                                                                        flex: 1, 
                                                                        fontSize: 11, 
                                                                        height: 20, 
                                                                        padding: '2px 6px',
                                                                        background: 'var(--theia-input-background)',
                                                                        color: 'var(--theia-input-foreground)',
                                                                        border: '1px solid var(--theia-input-border)'
                                                                    }}
                                                                />
                                                                <button
                                                                    type="button"
                                                                    onClick={(e) => {
                                                                        e.stopPropagation();
                                                                        setShowTreeIndex(showTree ? null : idx);
                                                                    }}
                                                                    style={{
                                                                        padding: '2px 6px',
                                                                        fontSize: 8,
                                                                        cursor: 'pointer',
                                                                        height: 20,
                                                                        background: 'var(--theia-button-background)',
                                                                        color: 'var(--theia-button-foreground)',
                                                                        border: 'none',
                                                                        borderRadius: 2
                                                                    }}
                                                                >
                                                                    ▼
                                                                </button>
                                                                
                                                                {showTree && (
                                                                    <div 
                                                                        className="adm-tree-popup"
                                                                        tabIndex={-1}
                                                                        style={{
                                                                            position: 'absolute',
                                                                            top: 24,
                                                                            left: 0,
                                                                            right: 0,
                                                                            maxHeight: 180,
                                                                            overflowY: 'auto',
                                                                            background: 'var(--theia-editor-background, #fff)',
                                                                            color: 'var(--theia-foreground, #333)',
                                                                            border: '1px solid var(--theia-border, #ccc)',
                                                                            borderRadius: 3,
                                                                            boxShadow: '0 2px 8px rgba(0,0,0,0.15)',
                                                                            zIndex: 999,
                                                                            padding: 6
                                                                        }}
                                                                    >
                                                                        <TreeSelect 
                                                                            tree={symbolTree} 
                                                                            onSelect={(path, type) => {
                                                                                let val = path;
                                                                                if (type === 'folder') {
                                                                                    // Append wildcard for folders
                                                                                    val = path === '*' ? '*' : `${path}\\*`;
                                                                                }
                                                                                setEditValue(val);
                                                                                handleSaveFilterRule(idx, val);
                                                                            }} 
                                                                        />
                                                                    </div>
                                                                )}
                                                            </div>
                                                        ) : (
                                                            <span>{rule}</span>
                                                        )}
                                                    </div>
                                                );
                                            })}
                                            
                                            {/* click to add... placeholder row */}
                                            {editingIndex === null && (
                                                <div 
                                                    style={{ 
                                                        display: 'flex', 
                                                        alignItems: 'center', 
                                                        padding: '4px 8px',
                                                        color: 'var(--theia-successForeground, #2ecc71)',
                                                        cursor: 'pointer',
                                                        fontSize: 12
                                                    }}
                                                    onClick={handleAddFilterRule}
                                                >
                                                    <span style={{ marginRight: 6 }}>➕</span>
                                                    <span>click to add...</span>
                                                </div>
                                            )}
                                        </div>
                                    </div>

                                    {/* Allow importing symbols settings checkbox */}
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 6, marginTop: 8 }}>
                                        <input 
                                            type="checkbox" 
                                            id="allow_import" 
                                            checked={allowImport} 
                                            onChange={e => setAllowImport(e.target.checked)} 
                                        />
                                        <label htmlFor="allow_import" style={{ cursor: 'pointer', fontSize: 11, userSelect: 'none', margin: 0 }}>
                                            Allow importing symbol settings
                                        </label>
                                    </div>
                                </div>
                            )}

                            {modalActiveTab === 'translations' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-end', background: 'var(--theia-editor-background)', padding: 10, border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <div className="adm-form-row" style={{ flex: 2 }}>
                                            <label>Platform Symbol</label>
                                            <input className="adm-input" placeholder="e.g. EURUSD or *" value={newRule.symbol} onChange={e => setNewRule({ ...newRule, symbol: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 2 }}>
                                            <label>Source Symbol</label>
                                            <input className="adm-input" placeholder="e.g. EURUSD_pro or *.pro" value={newRule.source} onChange={e => setNewRule({ ...newRule, source: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Bid Adj (Pts)</label>
                                            <input className="adm-input" type="number" placeholder="e.g. -2" value={newRule.bid_adj} onChange={e => setNewRule({ ...newRule, bid_adj: parseInt(e.target.value) || 0 })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Ask Adj (Pts)</label>
                                            <input className="adm-input" type="number" placeholder="e.g. 2" value={newRule.ask_adj} onChange={e => setNewRule({ ...newRule, ask_adj: parseInt(e.target.value) || 0 })} />
                                        </div>
                                        <button type="button" className="adm-btn adm-btn-primary" style={{ height: 26 }} onClick={handleAddRule}>
                                            <i className="codicon codicon-add" /> Add
                                        </button>
                                    </div>

                                    <div style={{ maxHeight: '25vh', overflowY: 'auto', border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <table className="adm-table" style={{ margin: 0 }}>
                                            <thead>
                                                <tr>
                                                    <th>Platform Symbol</th>
                                                    <th>Source Symbol</th>
                                                    <th>Bid Adj (Points)</th>
                                                    <th>Ask Adj (Points)</th>
                                                    <th style={{ width: 60 }}>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {translations.length === 0 ? (
                                                    <tr>
                                                        <td colSpan={5} style={{ textAlign: 'center', opacity: 0.6, padding: 12 }}>
                                                            No symbol translations configured. Direct matching (* &lt;- *) active.
                                                        </td>
                                                    </tr>
                                                ) : (
                                                    translations.map((t, idx) => (
                                                        <tr key={idx}>
                                                            <td>{t.symbol}</td>
                                                            <td>{t.source}</td>
                                                            <td>{t.bid_adj}</td>
                                                            <td>{t.ask_adj}</td>
                                                            <td>
                                                                <button type="button" className="adm-btn" style={{ padding: '2px 6px', color: 'var(--theia-errorForeground)' }} onClick={() => handleRemoveRule(idx)}>
                                                                    <i className="codicon codicon-trash" /> Delete
                                                                </button>
                                                            </td>
                                                        </tr>
                                                    ))
                                                )}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            )}

                            {modalActiveTab === 'parameters' && (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-end', background: 'var(--theia-editor-background)', padding: 10, border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Parameter Key</label>
                                            <input className="adm-input" placeholder="e.g. Quotes Delay" value={newParam.key} onChange={e => setNewParam({ ...newParam, key: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Value</label>
                                            <input className="adm-input" placeholder="Value expression" value={newParam.val} onChange={e => setNewParam({ ...newParam, val: e.target.value })} />
                                        </div>
                                        <button type="button" className="adm-btn adm-btn-primary" style={{ height: 26 }} onClick={handleAddParam}>
                                            <i className="codicon codicon-add" /> Add Param
                                        </button>
                                    </div>

                                    <div style={{ maxHeight: '25vh', overflowY: 'auto', border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <table className="adm-table" style={{ margin: 0 }}>
                                            <thead>
                                                <tr>
                                                    <th>Parameter Name</th>
                                                    <th>Value</th>
                                                    <th style={{ width: 60 }}>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {parameters.map((p, idx) => (
                                                    <tr key={idx}>
                                                        <td><strong>{p.key}</strong></td>
                                                        <td>
                                                            <input className="adm-input" style={{ width: '100%', border: 'none', background: 'transparent', height: 20, padding: 0 }} value={p.val} onChange={e => {
                                                                const updated = [...parameters];
                                                                updated[idx].val = e.target.value;
                                                                setParameters(updated);
                                                            }} />
                                                        </td>
                                                        <td>
                                                            <button type="button" className="adm-btn" style={{ padding: '2px 6px', color: 'var(--theia-errorForeground)' }} onClick={() => handleRemoveParam(idx)}>
                                                                <i className="codicon codicon-trash" /> Delete
                                                            </button>
                                                        </td>
                                                    </tr>
                                                ))}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            )}
                        </div>

                        <div className="adm-modal-footer">
                            <button type="submit" className="adm-btn adm-btn-primary">{modalMode === 'create' ? 'Add Feed Connector' : 'Save Changes'}</button>
                            <button type="button" className="adm-btn" onClick={() => setShowModal(false)}>Cancel</button>
                        </div>
                    </form>
                </div>
            )}

            <div className="adm-statusbar">
                <span>Total Configured Feeds: {feeds.length}</span>
                <span className="adm-sep">|</span>
                <span style={{ color: STATUS_COLOR.connected }}>Running: {feeds.filter(f => f.is_active).length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-deals-dealspage-tsx'></a>
### 63. `browser/modules/deals/DealsPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';

interface Deal {
    id: string;
    deal: number;
    order: number;
    login: number;
    symbol: string;
    action: 'BUY' | 'SELL';
    entry: 'IN' | 'OUT' | 'IN/OUT';
    volume: number;
    price: number;
    profit: number;
    swap: number;
    commission: number;
    time: string;
    comment: string;
    reason: string;
}

const MOCK_DEALS: Deal[] = [
    { id: '1', deal: 30001, order: 10001, login: 50080, symbol: 'EURUSD', action: 'BUY',  entry: 'IN',  volume: 0.10, price: 1.08250, profit: 0.00,   swap: 0.00,  commission: -0.50, time: '2026-08-19 10:22:11', comment: '',          reason: 'CLIENT' },
    { id: '2', deal: 30002, order: 10002, login: 50080, symbol: 'EURUSD', action: 'SELL', entry: 'OUT', volume: 0.10, price: 1.08340, profit: 9.00,   swap: -0.32, commission: -0.50, time: '2026-08-19 15:44:22', comment: '',          reason: 'CLIENT' },
    { id: '3', deal: 30003, order: 20003, login: 50082, symbol: 'GBPUSD', action: 'SELL', entry: 'IN',  volume: 0.50, price: 1.27100, profit: 0.00,   swap: 0.00,  commission: -2.50, time: '2026-08-19 14:22:10', comment: 'EA order',  reason: 'EXPERT' },
];

export function DealsPage(): React.ReactElement {
    const [deals] = React.useState<Deal[]>(MOCK_DEALS);
    const [selected, setSelected] = React.useState<string | null>(null);
    const [filter, setFilter] = React.useState('');
    const [dateFrom, setDateFrom] = React.useState('');
    const [dateTo, setDateTo] = React.useState('');

    const filtered = deals.filter(d =>
        String(d.login).includes(filter) ||
        d.symbol.toLowerCase().includes(filter.toLowerCase()) ||
        String(d.deal).includes(filter)
    );

    const totalProfit = filtered.reduce((s, d) => s + d.profit, 0);
    const totalComm   = filtered.reduce((s, d) => s + d.commission, 0);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input className="adm-search" placeholder="Filter by login, symbol, deal..." value={filter} onChange={e => setFilter(e.target.value)} />
                </div>
                <div className="adm-toolbar-sep" />
                <label style={{ fontSize: 11, opacity: 0.7 }}>From:</label>
                <input type="date" className="adm-input" style={{ width: 130 }} value={dateFrom} onChange={e => setDateFrom(e.target.value)} />
                <label style={{ fontSize: 11, opacity: 0.7 }}>To:</label>
                <input type="date" className="adm-input" style={{ width: 130 }} value={dateTo} onChange={e => setDateTo(e.target.value)} />
                <button className="adm-btn adm-btn-primary"><i className="codicon codicon-search" /> Request</button>
                <div className="adm-toolbar-sep" />
                <button className="adm-btn"><i className="codicon codicon-export" /> Export</button>
            </div>

            <div className="adm-table-wrap">
                <table className="adm-table">
                    <thead>
                        <tr>
                            <th>Deal #</th>
                            <th>Order #</th>
                            <th>Login</th>
                            <th>Symbol</th>
                            <th>Action</th>
                            <th>Entry</th>
                            <th>Volume</th>
                            <th>Price</th>
                            <th>Profit</th>
                            <th>Swap</th>
                            <th>Commission</th>
                            <th>Reason</th>
                            <th>Time</th>
                            <th>Comment</th>
                        </tr>
                    </thead>
                    <tbody>
                        {filtered.map(d => (
                            <tr key={d.id} className={selected === d.id ? 'selected' : ''} onClick={() => setSelected(d.id)}>
                                <td><strong>{d.deal}</strong></td>
                                <td>{d.order}</td>
                                <td>{d.login}</td>
                                <td><strong>{d.symbol}</strong></td>
                                <td><span className={`adm-side-badge ${d.action.toLowerCase()}`}>{d.action}</span></td>
                                <td><span className="adm-tag">{d.entry}</span></td>
                                <td>{d.volume.toFixed(2)}</td>
                                <td className="adm-num">{d.price.toFixed(5)}</td>
                                <td className={`adm-num ${d.profit >= 0 ? 'adm-pos' : 'adm-neg'}`}>{d.profit >= 0 ? '+' : ''}{d.profit.toFixed(2)}</td>
                                <td className="adm-num">{d.swap.toFixed(2)}</td>
                                <td className="adm-num adm-neg">{d.commission.toFixed(2)}</td>
                                <td>{d.reason}</td>
                                <td>{d.time}</td>
                                <td>{d.comment}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="adm-statusbar">
                <span>Deals: {filtered.length}</span>
                <span className="adm-sep">|</span>
                <span className={totalProfit >= 0 ? 'adm-pos' : 'adm-neg'}>Profit: {totalProfit >= 0 ? '+' : ''}{totalProfit.toFixed(2)}</span>
                <span className="adm-sep">|</span>
                <span className="adm-neg">Commission: {totalComm.toFixed(2)}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-gateways-gatewayspage-tsx'></a>
### 63. `browser/modules/gateways/GatewaysPage.tsx`

```tsx
import * as React from 'react';
import { API } from '../api';

const STATUS_COLOR: Record<string, string> = {
    connected: 'var(--theia-successForeground)',
    disconnected: 'var(--theia-descriptionForeground)',
    error: 'var(--theia-errorForeground)',
};
const TYPE_COLOR: Record<string, string> = {
    FIX: '#3498db', MT5: '#9b59b6', REST: '#27ae60', Custom: '#f39c12'
};

export function GatewaysPage(): React.ReactElement {
    const [gateways, setGateways] = React.useState<any[]>([]);
    const [availableGroups, setAvailableGroups] = React.useState<any[]>([]);
    const [selected, setSelected] = React.useState<number | null>(null);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Modal state
    const [showModal, setShowModal] = React.useState(false);
    const [modalMode, setModalMode] = React.useState<'create' | 'edit'>('create');
    const [activeTab, setActiveTab] = React.useState<'general' | 'groups' | 'translations'>('general');
    
    const [gatewayForm, setGatewayForm] = React.useState({
        id: null as number | null,
        name: '',
        type: 'FIX',
        host: '',
        port: '',
        username: '',
        api_key: '',
        is_active: true
    });
    
    // Groups state matching standard MT5 tab settings
    const [gatewayGroups, setGatewayGroups] = React.useState<string[]>(['*']);
    const [allowImportBalances, setAllowImportBalances] = React.useState(false);
    const [selectedGroupIdx, setSelectedGroupIdx] = React.useState<number | null>(null);
    const [editingGroupIdx, setEditingGroupIdx] = React.useState<number | null>(null);
    const [editingGroupVal, setEditingGroupVal] = React.useState('');

    // Translations state
    const [translations, setTranslations] = React.useState<any[]>([]);
    const [newRule, setNewRule] = React.useState({
        symbol: '',
        source: '',
        bid_adj: 0,
        ask_adj: 0
    });
    
    const [modalError, setModalError] = React.useState<string | null>(null);

    const loadGateways = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getGateways();
            // Filter out price feeders (they will be displayed on DataFeedsPage.tsx)
            const filtered = data.filter((g: any) => !g.type.startsWith('Feeder_'));
            setGateways(filtered);
        } catch (err: any) {
            setError(err.message || 'Failed to load gateways.');
        } finally {
            setLoading(false);
        }
    };

    const loadDbGroups = async () => {
        try {
            const data = await API.getGroups();
            setAvailableGroups(data);
        } catch (e) {
            console.error('Failed to load groups for gateway settings dropdown:', e);
        }
    };

    React.useEffect(() => {
        loadGateways();
        loadDbGroups();
    }, []);

    const openCreateModal = () => {
        setModalMode('create');
        setActiveTab('general');
        setGatewayForm({
            id: null,
            name: '',
            type: 'FIX',
            host: '',
            port: '',
            username: '',
            api_key: '',
            is_active: true
        });
        setTranslations([]);
        setGatewayGroups(['*']);
        setAllowImportBalances(false);
        setSelectedGroupIdx(null);
        setEditingGroupIdx(null);
        setEditingGroupVal('');
        setModalError(null);
        setShowModal(true);
    };

    const openEditModal = (g: any) => {
        setModalMode('edit');
        setActiveTab('general');
        setGatewayForm({
            id: g.id,
            name: g.name,
            type: g.type,
            host: g.host || '',
            port: g.port ? String(g.port) : '',
            username: g.username || '',
            api_key: g.api_key || '',
            is_active: g.is_active === 1
        });
        
        let rules = [];
        let groups = ['*'];
        let allow_import = false;
        
        if (g.settings_json) {
            try {
                const parsed = JSON.parse(g.settings_json);
                rules = parsed.translations || [];
                if (parsed.groups) {
                    groups = parsed.groups;
                }
                if (parsed.allow_import_balances !== undefined) {
                    allow_import = parsed.allow_import_balances;
                }
            } catch (err) {
                // ignore
            }
        }
        setTranslations(rules);
        setGatewayGroups(groups);
        setAllowImportBalances(allow_import);
        setSelectedGroupIdx(null);
        setEditingGroupIdx(null);
        setEditingGroupVal('');
        setModalError(null);
        setShowModal(true);
    };

    const handleAddRule = () => {
        if (!newRule.symbol.trim() || !newRule.source.trim()) {
            alert('Symbol and Source pattern are required.');
            return;
        }
        setTranslations([...translations, {
            symbol: newRule.symbol.trim(),
            source: newRule.source.trim(),
            bid_adj: Number(newRule.bid_adj) || 0,
            ask_adj: Number(newRule.ask_adj) || 0
        }]);
        setNewRule({ symbol: '', source: '', bid_adj: 0, ask_adj: 0 });
    };

    const handleRemoveRule = (idx: number) => {
        setTranslations(translations.filter((_, i) => i !== idx));
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setModalError(null);
        
        const payload = {
            name: gatewayForm.name,
            type: gatewayForm.type,
            host: gatewayForm.host || undefined,
            port: gatewayForm.port ? parseInt(gatewayForm.port) : undefined,
            username: gatewayForm.username || undefined,
            api_key: gatewayForm.api_key || undefined,
            is_active: gatewayForm.is_active,
            settings_json: JSON.stringify({ 
                translations, 
                groups: gatewayGroups, 
                allow_import_balances: allowImportBalances 
            })
        };

        try {
            if (modalMode === 'create') {
                await API.createGateway(payload);
            } else {
                await API.updateGateway(gatewayForm.id!, payload);
            }
            setShowModal(false);
            await loadGateways();
        } catch (err: any) {
            setModalError(err.message || 'Failed to save gateway.');
        }
    };

    const handleTestGateway = async () => {
        if (!selected) return;
        setError(null);
        try {
            const resp = await API.testGateway(selected);
            alert(`Gateway Connection Test: ${resp.message}`);
        } catch (err: any) {
            setError(err.message || 'Gateway test failed.');
        }
    };

    const selectedGateway = gateways.find(g => g.id === selected);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn adm-btn-primary" onClick={openCreateModal}>
                    <i className="codicon codicon-add" /> Add Gateway
                </button>
                <button className="adm-btn" disabled={!selected} onClick={() => selectedGateway && openEditModal(selectedGateway)}>
                    <i className="codicon codicon-edit" /> Edit Gateway
                </button>
                <button className="adm-btn" disabled={!selected} onClick={handleTestGateway}>
                    <i className="codicon codicon-beaker" /> Test Connection
                </button>
                <button className="adm-btn" onClick={loadGateways} title="Reload data">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading gateways...</div>
                ) : gateways.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No gateways configured. Add a gateway to route orders to external liquidity providers.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th></th>
                                <th>Name</th>
                                <th>Type</th>
                                <th>Host / Server</th>
                                <th>Port</th>
                                <th>Username / Account</th>
                                <th>Status</th>
                                <th>Created At</th>
                            </tr>
                        </thead>
                        <tbody>
                            {gateways.map(g => {
                                const statusStr = g.is_active ? 'connected' : 'disconnected';
                                return (
                                    <tr key={g.id} className={selected === g.id ? 'selected' : ''} onClick={() => setSelected(g.id)} onDoubleClick={() => openEditModal(g)}>
                                        <td><span className={`adm-status-dot ${g.is_active ? 'online' : 'offline'}`} /></td>
                                        <td><strong>{g.name}</strong></td>
                                        <td><span className="adm-tag" style={{ color: TYPE_COLOR[g.type] || '#ccc', border: `1px solid ${(TYPE_COLOR[g.type] || '#ccc')}55` }}>{g.type}</span></td>
                                        <td><code className="adm-code">{g.host || '—'}</code></td>
                                        <td>{g.port || '—'}</td>
                                        <td>{g.username || '—'}</td>
                                        <td style={{ color: STATUS_COLOR[statusStr] }}>{statusStr}</td>
                                        <td>{g.created_at || '—'}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                )}
            </div>

            {showModal && (
                <div className="adm-modal-overlay" onClick={() => setShowModal(false)}>
                    <form className="adm-modal" style={{ width: 750, height: '65vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }} onClick={e => e.stopPropagation()} onSubmit={handleSubmit}>
                        <div className="adm-modal-header">
                            <h2>{modalMode === 'create' ? 'Add Liquidity Gateway' : `Edit Gateway: ${gatewayForm.name}`}</h2>
                            <button type="button" className="adm-modal-close" onClick={() => setShowModal(false)}>×</button>
                        </div>
                        
                        {/* Tab Switcher */}
                        <div className="adm-tabs" style={{ padding: '0 16px', borderBottom: '1px solid var(--theia-border)', flexShrink: 0 }}>
                            <button type="button" className={`adm-tab ${activeTab === 'general' ? 'active' : ''}`} onClick={() => setActiveTab('general')}>Common</button>
                            <button type="button" className={`adm-tab ${activeTab === 'groups' ? 'active' : ''}`} onClick={() => setActiveTab('groups')}>Groups</button>
                            <button type="button" className={`adm-tab ${activeTab === 'translations' ? 'active' : ''}`} onClick={() => setActiveTab('translations')}>Translations</button>
                        </div>

                        <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', padding: 16 }}>
                            {modalError && (
                                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 12px 0' }}>
                                    <i className="codicon codicon-error" /> {modalError}
                                </div>
                            )}

                            {activeTab === 'general' ? (
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16 }}>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                        <div className="adm-form-row">
                                            <label>Gateway Name</label>
                                            <input className="adm-input" required placeholder="e.g. LP-Gateway-1" value={gatewayForm.name} onChange={e => setGatewayForm({ ...gatewayForm, name: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Type</label>
                                            <select className="adm-select" value={gatewayForm.type} onChange={e => setGatewayForm({ ...gatewayForm, type: e.target.value })}>
                                                <option value="FIX">FIX Protocol</option>
                                                <option value="MT5">MetaTrader 5 Bridge</option>
                                                <option value="REST">REST API Gateway</option>
                                                <option value="Custom">Custom Provider</option>
                                            </select>
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Host / Hostname</label>
                                            <input className="adm-input" placeholder="e.g. localhost or lp.broker.com" value={gatewayForm.host} onChange={e => setGatewayForm({ ...gatewayForm, host: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Port</label>
                                            <input className="adm-input" type="number" placeholder="e.g. 8003" value={gatewayForm.port} onChange={e => setGatewayForm({ ...gatewayForm, port: e.target.value })} />
                                        </div>
                                    </div>
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                        <div className="adm-form-row">
                                            <label>Username / Account ID</label>
                                            <input className="adm-input" placeholder="Login ID" value={gatewayForm.username} onChange={e => setGatewayForm({ ...gatewayForm, username: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>API Key / Password</label>
                                            <input className="adm-input" type="password" placeholder="Access key/token" value={gatewayForm.api_key} onChange={e => setGatewayForm({ ...gatewayForm, api_key: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ marginTop: 24, flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                                            <input type="checkbox" id="gw_active" checked={gatewayForm.is_active} onChange={e => setGatewayForm({ ...gatewayForm, is_active: e.target.checked })} />
                                            <label htmlFor="gw_active" style={{ cursor: 'pointer', margin: 0 }}>Enable Gateway Connection</label>
                                        </div>
                                    </div>
                                </div>
                            ) : activeTab === 'groups' ? (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)', borderBottom: '1px solid var(--theia-border)', paddingBottom: 4 }}>
                                        Please specify the client groups whose trade operations shall be processed by this gateway.
                                    </div>
                                    <div style={{ display: 'flex', gap: 16, height: 260 }}>
                                        {/* Left Control Buttons */}
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, width: 80 }}>
                                            <button 
                                                type="button" 
                                                className="adm-btn"
                                                onClick={() => {
                                                    const nextIdx = gatewayGroups.length;
                                                    setGatewayGroups([...gatewayGroups, 'new_group\\*']);
                                                    setSelectedGroupIdx(nextIdx);
                                                    setEditingGroupIdx(nextIdx);
                                                    setEditingGroupVal('new_group\\*');
                                                }}
                                            >
                                                Add
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn"
                                                disabled={selectedGroupIdx === null}
                                                onClick={() => {
                                                    if (selectedGroupIdx !== null) {
                                                        setEditingGroupIdx(selectedGroupIdx);
                                                        setEditingGroupVal(gatewayGroups[selectedGroupIdx]);
                                                    }
                                                }}
                                            >
                                                Edit
                                            </button>
                                            <button 
                                                type="button" 
                                                className="adm-btn adm-btn-danger"
                                                disabled={selectedGroupIdx === null}
                                                onClick={() => {
                                                    if (selectedGroupIdx !== null) {
                                                        const updated = gatewayGroups.filter((_, idx) => idx !== selectedGroupIdx);
                                                        setGatewayGroups(updated);
                                                        setSelectedGroupIdx(null);
                                                        setEditingGroupIdx(null);
                                                    }
                                                }}
                                            >
                                                Delete
                                            </button>
                                        </div>

                                        {/* Right List Box container */}
                                        <div style={{ 
                                            flex: 1, 
                                            border: '1px solid var(--theia-border)', 
                                            borderRadius: 4, 
                                            background: 'var(--theia-input-background)',
                                            overflowY: 'auto',
                                            display: 'flex',
                                            flexDirection: 'column'
                                        }}>
                                            {gatewayGroups.map((gStr, idx) => {
                                                const isSelected = selectedGroupIdx === idx;
                                                const isEditing = editingGroupIdx === idx;
                                                
                                                if (isEditing) {
                                                    return (
                                                        <div key={idx} style={{ padding: '4px 8px', borderBottom: '1px solid var(--theia-border)', display: 'flex', gap: 8, alignItems: 'center' }}>
                                                            <input 
                                                                className="adm-input" 
                                                                style={{ flex: 1, height: 20, fontSize: 11 }}
                                                                value={editingGroupVal}
                                                                autoFocus
                                                                onChange={e => setEditingGroupVal(e.target.value)}
                                                                placeholder="e.g. real\*"
                                                                onKeyDown={e => {
                                                                    if (e.key === 'Enter') {
                                                                        const updated = [...gatewayGroups];
                                                                        updated[idx] = editingGroupVal.trim() || '*';
                                                                        setGatewayGroups(updated);
                                                                        setEditingGroupIdx(null);
                                                                    } else if (e.key === 'Escape') {
                                                                        setEditingGroupIdx(null);
                                                                    }
                                                                }}
                                                            />
                                                            <select
                                                                className="adm-select"
                                                                style={{ width: 180, height: 20, fontSize: 11 }}
                                                                value=""
                                                                onChange={e => {
                                                                    const chosen = e.target.value;
                                                                    if (chosen) {
                                                                        setEditingGroupVal(chosen);
                                                                        const updated = [...gatewayGroups];
                                                                        updated[idx] = chosen;
                                                                        setGatewayGroups(updated);
                                                                        setEditingGroupIdx(null);
                                                                    }
                                                                }}
                                                            >
                                                                <option value="">-- Select group... --</option>
                                                                <option value="*">* (All Groups)</option>
                                                                {availableGroups.map(g => (
                                                                    <option key={g.name} value={g.name}>{g.name}</option>
                                                                ))}
                                                            </select>
                                                            <button 
                                                                type="button"
                                                                className="adm-btn adm-btn-primary"
                                                                style={{ height: 20, padding: '0 8px', fontSize: 10, minWidth: 40 }}
                                                                onClick={() => {
                                                                    const updated = [...gatewayGroups];
                                                                    updated[idx] = editingGroupVal.trim() || '*';
                                                                    setGatewayGroups(updated);
                                                                    setEditingGroupIdx(null);
                                                                }}
                                                            >
                                                                Save
                                                            </button>
                                                        </div>
                                                    );
                                                }

                                                return (
                                                    <div 
                                                        key={idx}
                                                        style={{ 
                                                            display: 'flex', 
                                                            alignItems: 'center', 
                                                            gap: 8, 
                                                            padding: '6px 12px', 
                                                            cursor: 'pointer',
                                                            fontSize: 11,
                                                            borderBottom: '1px solid var(--theia-border)',
                                                            background: isSelected ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                            color: isSelected ? 'var(--theia-list-activeSelectionForeground)' : 'inherit'
                                                        }}
                                                        onClick={() => setSelectedGroupIdx(idx)}
                                                        onDoubleClick={() => {
                                                            setSelectedGroupIdx(idx);
                                                            setEditingGroupIdx(idx);
                                                            setEditingGroupVal(gStr);
                                                        }}
                                                    >
                                                        <i className="codicon codicon-organization" style={{ color: isSelected ? 'inherit' : '#3498db' }} />
                                                        <strong>{gStr}</strong>
                                                    </div>
                                                );
                                            })}

                                            <div 
                                                style={{ 
                                                    display: 'flex', 
                                                    alignItems: 'center', 
                                                    gap: 8, 
                                                    padding: '6px 12px', 
                                                    cursor: 'pointer',
                                                    fontSize: 11,
                                                    color: 'var(--theia-successForeground)'
                                                }}
                                                onClick={() => {
                                                    const nextIdx = gatewayGroups.length;
                                                    setGatewayGroups([...gatewayGroups, '']);
                                                    setSelectedGroupIdx(nextIdx);
                                                    setEditingGroupIdx(nextIdx);
                                                    setEditingGroupVal('');
                                                }}
                                            >
                                                <i className="codicon codicon-add" />
                                                <span>click to add...</span>
                                            </div>
                                        </div>
                                    </div>

                                    {/* Import traders balance option */}
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', fontSize: 11, marginTop: 4 }}>
                                        <input 
                                            type="checkbox" 
                                            checked={allowImportBalances} 
                                            onChange={e => setAllowImportBalances(e.target.checked)} 
                                        />
                                        Allow importing traders balances
                                    </label>
                                </div>
                            ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ display: 'flex', gap: 8, alignItems: 'flex-end', background: 'var(--theia-editor-background)', padding: 10, border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <div className="adm-form-row" style={{ flex: 2 }}>
                                            <label>Platform Symbol (Local)</label>
                                            <input className="adm-input" placeholder="e.g. EURUSD or *" value={newRule.symbol} onChange={e => setNewRule({ ...newRule, symbol: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 2 }}>
                                            <label>Source Symbol (External)</label>
                                            <input className="adm-input" placeholder="e.g. EURUSD.pro or *" value={newRule.source} onChange={e => setNewRule({ ...newRule, source: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Bid Adj (Pts)</label>
                                            <input className="adm-input" type="number" placeholder="e.g. -2" value={newRule.bid_adj} onChange={e => setNewRule({ ...newRule, bid_adj: parseInt(e.target.value) || 0 })} />
                                        </div>
                                        <div className="adm-form-row" style={{ flex: 1 }}>
                                            <label>Ask Adj (Pts)</label>
                                            <input className="adm-input" type="number" placeholder="e.g. 2" value={newRule.ask_adj} onChange={e => setNewRule({ ...newRule, ask_adj: parseInt(e.target.value) || 0 })} />
                                        </div>
                                        <button type="button" className="adm-btn adm-btn-primary" style={{ height: 26 }} onClick={handleAddRule}>
                                            <i className="codicon codicon-add" /> Add
                                        </button>
                                    </div>

                                    <div style={{ maxHeight: '25vh', overflowY: 'auto', border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                        <table className="adm-table" style={{ margin: 0 }}>
                                            <thead>
                                                <tr>
                                                    <th>Platform Symbol</th>
                                                    <th>Source Symbol</th>
                                                    <th>Bid Adj (Points)</th>
                                                    <th>Ask Adj (Points)</th>
                                                    <th style={{ width: 60 }}>Action</th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {translations.length === 0 ? (
                                                    <tr>
                                                        <td colSpan={5} style={{ textAlign: 'center', opacity: 0.6, padding: 12 }}>
                                                            No symbol translations configured. Direct matching (* &lt;- *) active.
                                                        </td>
                                                    </tr>
                                                ) : (
                                                    translations.map((t, idx) => (
                                                        <tr key={idx}>
                                                            <td>{t.symbol}</td>
                                                            <td>{t.source}</td>
                                                            <td>{t.bid_adj}</td>
                                                            <td>{t.ask_adj}</td>
                                                            <td>
                                                                <button type="button" className="adm-btn" style={{ padding: '2px 6px', color: 'var(--theia-errorForeground)' }} onClick={() => handleRemoveRule(idx)}>
                                                                    <i className="codicon codicon-trash" /> Delete
                                                                </button>
                                                            </td>
                                                        </tr>
                                                    ))
                                                )}
                                            </tbody>
                                        </table>
                                    </div>
                                </div>
                            )}
                        </div>
                        <div className="adm-modal-footer">
                            <button type="submit" className="adm-btn adm-btn-primary">{modalMode === 'create' ? 'Add Gateway' : 'Save Changes'}</button>
                            <button type="button" className="adm-btn" onClick={() => setShowModal(false)}>Cancel</button>
                        </div>
                    </form>
                </div>
            )}

            <div className="adm-statusbar">
                <span>Gateways: {gateways.length}</span>
                <span className="adm-sep">|</span>
                <span style={{ color: STATUS_COLOR.connected }}>Active: {gateways.filter(g => g.is_active).length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-groupspage-tsx'></a>
### 63. `browser/modules/groups/GroupsPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';
import { getGroupType, splitPathIntoSections, validateGroupName } from './groupTypeUtils';
import { GroupSettingsModal } from './modal/GroupSettingsModal';

const TYPE_COLORS: Record<string, string> = {
    Demo: '#3498db',
    Manager: '#9b59b6',
    Contest: '#e67e22',
    Coverage: '#16a085',
    Preliminary: '#e74c3c',
    Real: '#27ae60'
};

interface GroupsOverviewPageProps {
    selectedPath?: string;
}

export function GroupsOverviewPage({ selectedPath = '' }: GroupsOverviewPageProps): React.ReactElement {
    const [groups, setGroups] = React.useState<any[]>([]);
    const [gateways, setGateways] = React.useState<any[]>([]);
    const [selectedRows, setSelectedRows] = React.useState<string[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Active folder path (e.g. "", "demo", "real\IB")
    const [activeFolder, setActiveFolder] = React.useState(selectedPath);
    const [searchQuery, setSearchQuery] = React.useState('');

    // Context menu states
    const [contextMenu, setContextMenu] = React.useState<{ x: number, y: number, target: string | null } | null>(null);

    // Modal state
    const [modalGroup, setModalGroup] = React.useState<string | null>(null);
    const [showModal, setShowModal] = React.useState(false);
    const [addInitialName, setAddInitialName] = React.useState('');

    // Track active folder changes from sidebar tree clicks
    React.useEffect(() => {
        // Strip out "groups:" prefix if it exists from tree node ID
        let folder = selectedPath;
        if (folder.startsWith('groups:')) {
            folder = folder.substring(7);
        }
        setActiveFolder(folder);
    }, [selectedPath]);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const [gData, gwData] = await Promise.all([
                API.getGroups(),
                API.getGateways()
            ]);
            setGroups(gData);
            setGateways(gwData);
        } catch (err: any) {
            setError(err.message || 'Failed to fetch groups.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    // Left pane list of sections
    const folders = React.useMemo(() => {
        const set = new Set<string>();
        for (const g of groups) {
            const sections = splitPathIntoSections(g.name);
            let pathAccum = '';
            for (let i = 0; i < sections.length - 1; i++) {
                pathAccum = pathAccum ? `${pathAccum}\\${sections[i]}` : sections[i];
                set.add(pathAccum);
            }
        }
        return Array.from(set).sort();
    }, [groups]);

    // Explorer rows: filters children or groups inside the current active folder
    const explorerRows = React.useMemo(() => {
        const rowsMap = new Map<string, {
            type: 'folder' | 'group';
            name: string;      // Display label (e.g. "forex" or "preliminary")
            fullName: string;  // Full DB path (e.g. "demo\forex" or "preliminary")
            groupData?: any;   // DB record
        }>();

        const activeLower = activeFolder.toLowerCase();

        for (const g of groups) {
            const nameLower = g.name.toLowerCase();

            if (activeFolder === '') {
                // Root level: only show top-level folders or groups at root level
                if (g.name.includes('\\')) {
                    const firstFolder = g.name.split('\\')[0];
                    rowsMap.set(firstFolder.toLowerCase(), {
                        type: 'folder',
                        name: firstFolder,
                        fullName: firstFolder
                    });
                } else {
                    rowsMap.set(nameLower, {
                        type: 'group',
                        name: g.name,
                        fullName: g.name,
                        groupData: g
                    });
                }
            } else {
                // Inside a folder path
                if (nameLower.startsWith(activeLower + '\\')) {
                    const relativePath = g.name.substring(activeFolder.length + 1);
                    const parts = relativePath.split('\\');

                    if (parts.length === 1) {
                        rowsMap.set(nameLower, {
                            type: 'group',
                            name: parts[0],
                            fullName: g.name,
                            groupData: g
                        });
                    } else {
                        const subfolderName = parts[0];
                        const subfolderFullName = `${activeFolder}\\${subfolderName}`;
                        rowsMap.set(subfolderFullName.toLowerCase(), {
                            type: 'folder',
                            name: subfolderName,
                            fullName: subfolderFullName
                        });
                    }
                }
            }
        }

        let result = Array.from(rowsMap.values());
        if (searchQuery) {
            result = result.filter(r => r.name.toLowerCase().includes(searchQuery.toLowerCase()));
        }

        // Sort folders first, then groups alphabetically
        return result.sort((a, b) => {
            if (a.type !== b.type) {
                return a.type === 'folder' ? -1 : 1;
            }
            return a.name.localeCompare(b.name);
        });
    }, [groups, activeFolder, searchQuery]);

    const handleSelectRow = (fullName: string, type: 'folder' | 'group', e: React.MouseEvent) => {
        if (e.ctrlKey || e.metaKey) {
            if (selectedRows.includes(fullName)) {
                setSelectedRows(prev => prev.filter(r => r !== fullName));
            } else {
                setSelectedRows(prev => [...prev, fullName]);
            }
        } else if (e.shiftKey && selectedRows.length > 0) {
            const lastSelected = selectedRows[selectedRows.length - 1];
            const lastIdx = explorerRows.findIndex(r => r.fullName === lastSelected);
            const currentIdx = explorerRows.findIndex(r => r.fullName === fullName);
            if (lastIdx !== -1 && currentIdx !== -1) {
                const start = Math.min(lastIdx, currentIdx);
                const end = Math.max(lastIdx, currentIdx);
                const range = explorerRows.slice(start, end + 1).map(r => r.fullName);
                setSelectedRows(prev => Array.from(new Set([...prev, ...range])));
            }
        } else {
            setSelectedRows([fullName]);
        }
    };

    const handleRowDoubleClick = (row: any) => {
        if (row.type === 'folder') {
            setActiveFolder(row.fullName);
            setSelectedRows([]);
        } else {
            handleEdit(row.fullName);
        }
    };

    const handleEdit = (name?: string) => {
        const target = name || selectedRows[0];
        if (!target) return;
        // Verify it is a group, not a virtual folder
        const isGroup = groups.some(g => g.name === target);
        if (!isGroup) return;

        setModalGroup(target);
        setAddInitialName('');
        setShowModal(true);
    };

    const handleAdd = () => {
        setModalGroup(null);
        // Pre-fill path prefix if inside a folder
        setAddInitialName(activeFolder ? `${activeFolder}\\` : '');
        setShowModal(true);
    };

    const handleDelete = async () => {
        if (selectedRows.length === 0) return;
        
        // Filter out virtual folders, can only delete groups
        const targetGroups = selectedRows.filter(r => groups.some(g => g.name === r));
        if (targetGroups.length === 0) {
            alert("Please select actual group records to delete, virtual folders are deleted dynamically when empty.");
            return;
        }

        const confirmMsg = targetGroups.length === 1 
            ? `Are you sure you want to delete the group "${targetGroups[0]}"?`
            : `Are you sure you want to delete the ${targetGroups.length} selected groups?`;
            
        if (!confirm(confirmMsg)) return;

        setError(null);
        try {
            for (const name of targetGroups) {
                await API.deleteGroup(name);
            }
            setSelectedRows([]);
            await loadData();
        } catch (err: any) {
            setError(err.message || 'Failed to delete groups. Make sure no client accounts exist inside them.');
        }
    };

    const handleRightClick = (row: any, e: React.MouseEvent) => {
        e.preventDefault();
        if (!selectedRows.includes(row.fullName)) {
            setSelectedRows([row.fullName]);
        }
        setContextMenu({
            x: e.clientX,
            y: e.clientY,
            target: row.fullName
        });
    };

    React.useEffect(() => {
        const closeMenu = () => setContextMenu(null);
        window.addEventListener('click', closeMenu);
        return () => window.removeEventListener('click', closeMenu);
    }, []);

    const handleMove = (direction: 'up' | 'down') => {
        if (selectedRows.length !== 1) return;
        alert(`Moved row ${direction} on server.`);
    };

    const isSingleGroupSelected = selectedRows.length === 1 && groups.some(g => g.name === selectedRows[0]);

    return (
        <div className="adm-page" style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            {/* Main Action Toolbar */}
            <div className="adm-toolbar">
                <button type="button" className="adm-btn adm-btn-primary" onClick={handleAdd}>
                    <i className="codicon codicon-add" /> Add
                </button>
                <button type="button" className="adm-btn" disabled={!isSingleGroupSelected} onClick={() => handleEdit()}>
                    <i className="codicon codicon-edit" /> Edit
                </button>
                <button type="button" className="adm-btn adm-btn-danger" disabled={selectedRows.length === 0} onClick={handleDelete}>
                    <i className="codicon codicon-trash" /> Delete
                </button>
                <button type="button" className="adm-btn" onClick={loadData} title="Reload list">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>

                {activeFolder && (
                    <button type="button" className="adm-btn" onClick={() => {
                        const parts = activeFolder.split('\\');
                        setActiveFolder(parts.slice(0, -1).join('\\'));
                        setSelectedRows([]);
                    }}>
                        <i className="codicon codicon-arrow-left" /> Up one level
                    </button>
                )}

                <div className="adm-toolbar-sep" />

                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input 
                        className="adm-search" 
                        placeholder="Search current view..." 
                        value={searchQuery}
                        onChange={e => setSearchQuery(e.target.value)}
                    />
                </div>
            </div>

            {/* Split View: Tree Nav Pane & Details Table */}
            <div className="adm-split-view" style={{ flex: 1, overflow: 'hidden' }}>
                
                {/* Left navigation tree pane */}
                <div className="adm-tree-pane" style={{ width: 220, borderRight: '1px solid var(--theia-border)', overflowY: 'auto', padding: 8 }}>
                    <div className="adm-tree-pane-header" style={{ fontWeight: 'bold', fontSize: 11, marginBottom: 8, opacity: 0.7 }}>
                        SECTIONS & FOLDERS
                    </div>
                    <div 
                        className={`adm-tree-pane-row ${activeFolder === '' ? 'active' : ''}`}
                        onClick={() => { setActiveFolder(''); setSelectedRows([]); }}
                    >
                        <i className="codicon codicon-home" style={{ marginRight: 6 }} />
                        <span>All Groups</span>
                    </div>

                    {folders.map(f => {
                        const parts = splitPathIntoSections(f);
                        const depth = parts.length - 1;
                        return (
                            <div 
                                key={f} 
                                className={`adm-tree-pane-row ${activeFolder === f ? 'active' : ''}`}
                                style={{ paddingLeft: `${8 + depth * 14}px` }}
                                onClick={() => { setActiveFolder(f); setSelectedRows([]); }}
                            >
                                <i className="codicon codicon-folder" style={{ marginRight: 6 }} />
                                <span>{parts[parts.length - 1]}</span>
                            </div>
                        );
                    })}
                </div>

                {/* Right Explorer-style Details Table */}
                <div className="adm-table-wrap" style={{ flex: 1, overflowY: 'auto' }}>
                    {error && (
                        <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '10px 16px' }}>
                            <i className="codicon codicon-error" /> {error}
                        </div>
                    )}

                    {loading ? (
                        <div style={{ padding: 30, textAlign: 'center', opacity: 0.7 }}>Loading groups...</div>
                    ) : explorerRows.length === 0 ? (
                        <div style={{ padding: 30, textAlign: 'center', opacity: 0.6 }}>This folder is empty.</div>
                    ) : (
                        <table className="adm-table">
                            <thead>
                                <tr>
                                    <th>Group</th>
                                    <th>Server</th>
                                    <th>Authorization</th>
                                    <th>Currency</th>
                                    <th>Default Gateway</th>
                                </tr>
                            </thead>
                            <tbody>
                                {explorerRows.map(row => {
                                    const isSelected = selectedRows.includes(row.fullName);
                                    
                                    if (row.type === 'folder') {
                                        return (
                                            <tr 
                                                key={row.fullName} 
                                                className={isSelected ? 'selected' : ''}
                                                onClick={e => handleSelectRow(row.fullName, 'folder', e)}
                                                onDoubleClick={() => handleRowDoubleClick(row)}
                                                onContextMenu={e => handleRightClick(row, e)}
                                            >
                                                <td>
                                                    <i className="codicon codicon-folder" style={{ color: '#f1c40f', marginRight: 6 }} />
                                                    <strong>{row.name}</strong>
                                                </td>
                                                <td>—</td>
                                                <td>—</td>
                                                <td>—</td>
                                                <td>—</td>
                                            </tr>
                                        );
                                    }

                                    // Render Group Row
                                    const g = row.groupData;
                                    const type = getGroupType(g.name);
                                    
                                    let settings: any = {};
                                    if (g.settings_json) {
                                        try { settings = JSON.parse(g.settings_json); } catch {}
                                    }
                                    
                                    const authStr = settings.authentication || 'Normal';
                                    const currStr = settings.currency || 'USD';
                                    const serverStr = settings.trade_server || 'MetaQuotes-Demo';
                                    const isConnEnabled = settings.enable_connections !== false;

                                    const gwy = gateways.find(gw => gw.id === settings.gateway_id);
                                    const gwName = gwy ? gwy.name : (settings.gateway_id ? `Gateway #${settings.gateway_id}` : 'None (B-Book)');

                                    return (
                                        <tr 
                                            key={g.name} 
                                            className={`${isSelected ? 'selected' : ''} ${!isConnEnabled ? 'adm-row-disabled' : ''}`}
                                            onClick={e => handleSelectRow(row.fullName, 'group', e)}
                                            onDoubleClick={() => handleRowDoubleClick(row)}
                                            onContextMenu={e => handleRightClick(row, e)}
                                        >
                                            <td>
                                                <i className="codicon codicon-organization" style={{ color: TYPE_COLORS[type] || '#ccc', marginRight: 6 }} />
                                                <strong>{row.name}</strong>
                                            </td>
                                            <td>{serverStr}</td>
                                            <td>{authStr}</td>
                                            <td>{currStr}</td>
                                            <td>
                                                {settings.gateway_id ? (
                                                    <span className="adm-tag" style={{ color: '#3498db', border: '1px solid #3498db55' }}>
                                                        A-Book: {gwName}
                                                    </span>
                                                ) : (
                                                    <span style={{ opacity: 0.5 }}>B-Book Local</span>
                                                )}
                                            </td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    )}
                </div>
            </div>

            {/* Custom context menu popup */}
            {contextMenu && (
                <div 
                    className="adm-context-menu"
                    style={{ top: contextMenu.y, left: contextMenu.x }}
                    onClick={e => e.stopPropagation()}
                >
                    <button type="button" className="adm-context-item" disabled={!isSingleGroupSelected} onClick={() => handleEdit()}><i className="codicon codicon-edit" /> Edit Group</button>
                    <button type="button" className="adm-context-item" onClick={handleAdd}><i className="codicon codicon-add" /> Add Group</button>
                    <button type="button" className="adm-context-item adm-context-item-danger" disabled={selectedRows.length === 0} onClick={handleDelete}><i className="codicon codicon-trash" /> Delete</button>
                    <div className="adm-context-sep" />
                    <button type="button" className="adm-context-item" disabled={selectedRows.length !== 1} onClick={() => handleMove('up')}><i className="codicon codicon-arrow-up" /> Move Up</button>
                    <button type="button" className="adm-context-item" disabled={selectedRows.length !== 1} onClick={() => handleMove('down')}><i className="codicon codicon-arrow-down" /> Move Down</button>
                </div>
            )}

            {/* Rebuilt Group Settings Modal */}
            {showModal && (
                <GroupSettingsModal 
                    groupName={modalGroup}
                    initialName={addInitialName}
                    onClose={() => setShowModal(false)}
                    onSaved={loadData}
                />
            )}

            {/* Page Statusbar footer */}
            <div className="adm-statusbar">
                <span>Items: {explorerRows.length}</span>
                <span className="adm-sep">|</span>
                <span>Folders: {explorerRows.filter(r => r.type === 'folder').length}</span>
                <span className="adm-sep">|</span>
                <span>Groups: {explorerRows.filter(r => r.type === 'group').length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-grouptypeutils-ts'></a>
### 63. `browser/modules/groups/groupTypeUtils.ts`

```typescript
/**
 * Pure functions for MT5-Admin Groups module.
 * Single source of truth for group naming and path validations.
 */

export type GroupType = 'Demo' | 'Manager' | 'Contest' | 'Coverage' | 'Preliminary' | 'Real';

export function getGroupType(path: string): GroupType {
    if (!path) return 'Real';
    if (path.includes('demo')) {
        return 'Demo';
    }
    if (path.includes('manager')) {
        return 'Manager';
    }
    if (path.includes('contest')) {
        return 'Contest';
    }
    if (path.includes('coverage')) {
        return 'Coverage';
    }
    // Get last component of path
    const parts = path.split('\\');
    const leaf = parts[parts.length - 1];
    if (leaf === 'preliminary') {
        return 'Preliminary';
    }
    return 'Real';
}

export function validateGroupName(path: string): string | null {
    if (!path) return 'Group path cannot be empty.';
    
    // Check for invalid characters
    if (/[/:*?"<>|]/.test(path)) {
        return 'Group name cannot contain special characters like /, :, *, ?, ", <, >, |';
    }

    const pathLower = path.toLowerCase();
    const matches: string[] = [];
    if (pathLower.includes('demo')) matches.push('demo');
    if (pathLower.includes('manager')) matches.push('manager');
    if (pathLower.includes('contest')) matches.push('contest');
    if (pathLower.includes('coverage')) matches.push('coverage');
    if (pathLower.includes('preliminary')) matches.push('preliminary');

    if (matches.length > 1) {
        return `Warning: Group name mixes multiple type keywords (${matches.join(', ')}). This might cause unexpected type matching.`;
    }
    
    return null;
}

export function splitPathIntoSections(path: string): string[] {
    if (!path) return [];
    return path.split('\\').map(p => p.trim()).filter(Boolean);
}

```

---

<a id='browser-modules-groups-modal-groupdraftcontext-tsx'></a>
### 63. `browser/modules/groups/modal/GroupDraftContext.tsx`

```tsx
import * as React from 'react';

export interface SymbolRule {
    symbol: string;
    trade_allowed: boolean;
    spread_diff: number;
    commission_rate: number;
    margin_rate: number;

    // Common Tab Extra Settings
    enable_dom?: boolean;
    dom_limit?: string;
    use_default_spreads?: boolean;
    diff_balance?: string;
    use_default_volumes?: boolean;
    vol_min?: number;
    vol_step?: number;
    vol_max?: number;
    use_default_limit?: boolean;
    vol_limit?: number;

    // Trade Tab Extra Settings
    use_default_trade?: boolean;
    trade_mode?: string;
    filling_fok?: boolean;
    filling_ioc?: boolean;
    filling_boc?: boolean;
    expiration_gtc?: boolean;
    expiration_day?: boolean;
    expiration_time?: boolean;
    expiration_date?: boolean;
    use_default_trade_levels?: boolean;
    limit_stop_level?: number;
    freeze_level?: number;

    // Execution Tab Extra Settings
    use_default_execution?: boolean;
    exec_mode?: string;
    instant_max_time_dev?: number;
    instant_max_profit_dev?: number;
    instant_max_loss_dev?: number;
    instant_max_volume?: number;
    request_timeout?: number;
    request_confirm?: boolean;

    // Margin Tab Extra Settings
    use_default_margin?: boolean;
    initial_margin?: number;
    maintenance_margin?: number;
    hedged_margin?: number;
    calc_hedged_larger_leg?: boolean;
    exclude_long_pnl?: boolean;
    recalc_margin_eod?: boolean;
    margin_check_exec?: boolean;
    margin_check_sltp?: boolean;

    // Margin Rates Tab Extra Settings
    use_default_margin_rates?: boolean;
    liquidity_rate?: number;
    currency_rate?: number;
    rate_market_buy?: number;
    rate_market_sell?: number;
    rate_limit_buy?: number;
    rate_limit_sell?: number;
    rate_stop_buy?: number;
    rate_stop_sell?: number;
    rate_stop_limit_buy?: number;
    rate_stop_limit_sell?: number;

    // Swaps Tab Extra Settings
    swap_type?: string;
    swap_long?: number;
    swap_short?: number;
    swap_days_in_year?: number;
    swap_multiplier_mon?: number;
    swap_multiplier_tue?: number;
    swap_multiplier_wed?: number;
    swap_multiplier_thu?: number;
    swap_multiplier_fri?: number;
    swap_multiplier_sat?: number;
    swap_multiplier_sun?: number;
    swap_consider_holidays?: boolean;
}

export interface CommissionRule {
    name: string;
    symbols: string;
    rate: number;
    type: 'points' | 'percent' | 'money';
}

export interface GroupDraft {
    name: string;
    max_leverage: number;
    spread_override: number;
    currency: string;
    digits: number;
    trade_server: string;
    authentication: string;
    min_password_len: number;
    enable_cert_confirm: boolean;
    change_pass_first_login: boolean;
    otp_mode: 'disabled' | 'all' | 'web';
    force_otp: boolean;
    push_placed_orders: boolean;
    push_performed_deals: boolean;
    push_balance_operations: boolean;
    enable_connections: boolean;
    show_risk_warning: boolean;
    regulatory_restrictions: boolean;

    // Company Tab
    company: string;
    company_website: string;
    company_email: string;
    deposit_url: string;
    withdrawal_url: string;
    support_site: string;
    support_email: string;
    templates_folder: string;

    // News & Mail Tab
    news_mode: 'none' | 'headers' | 'full';
    news_categories: string;
    news_languages: string[];
    enable_internal_mail: boolean;

    // Permissions Tab
    max_symbols: number;
    max_positions: number;
    max_orders: number;
    available_history: string;
    interest_rate: number;
    default_deposit: number;
    default_leverage: number;
    trade_signals_mode: 'disabled' | 'all' | 'own_only';
    transfer_funds_mode: 'disabled' | 'same_details' | 'subgroup' | 'subgroup_name';
    enable_swaps: boolean;
    enable_trailing_stops: boolean;
    enable_ea_trading: boolean;
    fifo_rule: boolean;
    prohibit_hedge: boolean;
    deal_cost_calc: boolean;
    inactivity_days: number;

    // Margin Tab
    risk_management_model: 'netting' | 'hedging' | 'discount';
    margin_call: number;
    margin_stop_out: number;
    stop_out_mode: 'percent' | 'money';
    stop_out_hedged: boolean;
    compensate_negative_balance: boolean;
    withdraw_credit_after_comp: boolean;
    floating_leverage_profile: string;
    virtual_credit: number;
    unrealized_profit_mode: number;
    daily_fixed_profit_mode: number;
    release_fixed_profit: boolean;

    // Symbol & Commission Lists
    symbol_rules: SymbolRule[];
    commission_rules: CommissionRule[];

    // Reports Tab
    report_generation: 'off' | 'daily' | 'monthly' | 'both';
    generate_statements: boolean;
    send_statements_email: boolean;
    mail_server: string;
    send_copies_support: boolean;
    gateway_id?: number;
}

export const DEFAULT_DRAFT: GroupDraft = {
    name: '',
    max_leverage: 100,
    spread_override: 0,
    currency: 'USD',
    digits: 2,
    trade_server: 'MetaQuotes-Demo',
    authentication: 'Normal',
    min_password_len: 8,
    enable_cert_confirm: false,
    change_pass_first_login: false,
    otp_mode: 'disabled',
    force_otp: false,
    push_placed_orders: false,
    push_performed_deals: false,
    push_balance_operations: false,
    enable_connections: true,
    show_risk_warning: false,
    regulatory_restrictions: false,

    company: '',
    company_website: '',
    company_email: '',
    deposit_url: '',
    withdrawal_url: '',
    support_site: '',
    support_email: '',
    templates_folder: '',

    news_mode: 'full',
    news_categories: '',
    news_languages: ['Any language'],
    enable_internal_mail: true,

    max_symbols: 0,
    max_positions: 0,
    max_orders: 0,
    available_history: 'All',
    interest_rate: 0,
    default_deposit: 10000,
    default_leverage: 100,
    trade_signals_mode: 'all',
    transfer_funds_mode: 'same_details',
    enable_swaps: true,
    enable_trailing_stops: true,
    enable_ea_trading: true,
    fifo_rule: false,
    prohibit_hedge: false,
    deal_cost_calc: true,
    inactivity_days: 360,

    risk_management_model: 'hedging',
    margin_call: 50,
    margin_stop_out: 30,
    stop_out_mode: 'percent',
    stop_out_hedged: false,
    compensate_negative_balance: true,
    withdraw_credit_after_comp: true,
    floating_leverage_profile: 'Default',
    virtual_credit: 0,
    unrealized_profit_mode: 0,
    daily_fixed_profit_mode: 0,
    release_fixed_profit: false,

    symbol_rules: [{ symbol: '*', trade_allowed: true, spread_diff: 0, commission_rate: 0, margin_rate: 1.0 }],
    commission_rules: [],

    report_generation: 'off',
    generate_statements: false,
    send_statements_email: false,
    mail_server: 'Default',
    send_copies_support: false
};

interface GroupDraftContextProps {
    draft: GroupDraft;
    setDraft: React.Dispatch<React.SetStateAction<GroupDraft>>;
    errors: Record<string, string>;
    setErrors: React.Dispatch<React.SetStateAction<Record<string, string>>>;
    isEditing: boolean;
}

export const GroupDraftContext = React.createContext<GroupDraftContextProps | undefined>(undefined);

export function useGroupDraft() {
    const context = React.useContext(GroupDraftContext);
    if (!context) {
        throw new Error('useGroupDraft must be used within a GroupDraftProvider');
    }
    return context;
}

```

---

<a id='browser-modules-groups-modal-groupsettingsmodal-tsx'></a>
### 63. `browser/modules/groups/modal/GroupSettingsModal.tsx`

```tsx
import * as React from 'react';
import { GroupDraft, DEFAULT_DRAFT, GroupDraftContext } from './GroupDraftContext';
import { CommonTab } from './tabs/CommonTab';
import { GatewayTab } from './tabs/GatewayTab';
import { CompanyTab } from './tabs/CompanyTab';
import { NewsMailTab } from './tabs/NewsMailTab';
import { PermissionsTab } from './tabs/PermissionsTab';
import { MarginTab } from './tabs/MarginTab';
import { SymbolsTab } from './tabs/SymbolsTab';
import { CommissionsTab } from './tabs/CommissionsTab';
import { ReportsTab } from './tabs/ReportsTab';
import { API } from '../../api';

interface GroupSettingsModalProps {
    groupName: string | null; // null if adding new group
    initialName?: string;
    onClose: () => void;
    onSaved: () => void;
}

const TABS = [
    { id: 'common', label: 'Common' },
    { id: 'gateway', label: 'Gateway' },
    { id: 'company', label: 'Company' },
    { id: 'newsMail', label: 'News & Mail' },
    { id: 'permissions', label: 'Permissions' },
    { id: 'margin', label: 'Margin' },
    { id: 'symbols', label: 'Symbols' },
    { id: 'commissions', label: 'Commissions' },
    { id: 'reports', label: 'Reports' }
];

export function GroupSettingsModal({ groupName, initialName = '', onClose, onSaved }: GroupSettingsModalProps): React.ReactElement {
    const [draft, setDraft] = React.useState<GroupDraft>(DEFAULT_DRAFT);
    const [activeTab, setActiveTab] = React.useState('common');
    const [errors, setErrors] = React.useState<Record<string, string>>({});
    const [loading, setLoading] = React.useState(false);
    const [saveError, setSaveError] = React.useState<string | null>(null);

    const isEditing = !!groupName;

    // Load existing group details on edit mode
    React.useEffect(() => {
        if (groupName) {
            setLoading(true);
            API.getGroupDetail(groupName)
                .then(data => {
                    let parsedSettings: Partial<GroupDraft> = {};
                    if (data.settings_json) {
                        try {
                            parsedSettings = JSON.parse(data.settings_json);
                        } catch (e) {
                            console.error('Failed to parse settings JSON block', e);
                        }
                    }
                    
                    setDraft({
                        ...DEFAULT_DRAFT,
                        name: data.name,
                        max_leverage: data.max_leverage,
                        margin_call: data.margin_call,
                        margin_stop_out: data.margin_stop_out,
                        spread_override: data.spread_override,
                        ...parsedSettings
                    } as any);
                })
                .catch(err => {
                    setSaveError(err.message || 'Failed to fetch group details.');
                })
                .finally(() => {
                    setLoading(false);
                });
        } else if (initialName) {
            setDraft(prev => ({
                ...prev,
                name: initialName
            }));
        }
    }, [groupName, initialName]);

    // Validation check across all fields to place error badges on tab headings
    const validateAll = (): boolean => {
        const nextErrors: Record<string, string> = {};
        
        // 1. Common Tab
        if (!draft.name) {
            nextErrors.name = 'Group name is required';
        } else if (/[/:*?"<>|]/.test(draft.name)) {
            nextErrors.name = 'Group name cannot contain special characters like /, :, *, ?, ", <, >, |';
        }

        // 2. Company Tab
        if (!draft.company) {
            nextErrors.company = 'Company designation is required';
        }

        setErrors(nextErrors);
        return Object.keys(nextErrors).length === 0;
    };

    const tabHasErrors = (tabId: string): boolean => {
        if (tabId === 'common' && errors.name) return true;
        if (tabId === 'company' && errors.company) return true;
        return false;
    };

    const handleSave = async (e: React.FormEvent) => {
        e.preventDefault();
        setSaveError(null);

        if (!validateAll()) {
            setSaveError('Please correct validation errors on marked tabs before saving.');
            return;
        }

        setLoading(true);
        try {
            // Pack settings JSON string
            const settingsData = { ...draft } as any;
            // Avoid duplicate name/leverages in settings JSON block to keep DB cleaner
            delete settingsData.name;
            delete settingsData.max_leverage;
            delete settingsData.margin_call;
            delete settingsData.margin_stop_out;
            delete settingsData.spread_override;

            const payload = {
                name: draft.name,
                max_leverage: draft.max_leverage,
                margin_call: draft.margin_call,
                margin_stop_out: draft.margin_stop_out,
                spread_override: draft.spread_override,
                settings_json: JSON.stringify(settingsData)
            };

            if (isEditing) {
                await API.updateGroup(groupName!, payload);
            } else {
                await API.createGroup(payload);
            }

            onSaved();
            onClose();
        } catch (err: any) {
            setSaveError(err.message || 'Failed to save group details.');
        } finally {
            setLoading(false);
        }
    };

    const renderActiveTabContent = () => {
        switch (activeTab) {
            case 'common': return <CommonTab />;
            case 'gateway': return <GatewayTab />;
            case 'company': return <CompanyTab />;
            case 'newsMail': return <NewsMailTab />;
            case 'permissions': return <PermissionsTab />;
            case 'margin': return <MarginTab />;
            case 'symbols': return <SymbolsTab />;
            case 'commissions': return <CommissionsTab />;
            case 'reports': return <ReportsTab />;
            default: return <CommonTab />;
        }
    };

    return (
        <GroupDraftContext.Provider value={{ draft, setDraft, errors, setErrors, isEditing }}>
            <div className="adm-modal-overlay" onClick={onClose}>
                <div className="adm-modal" style={{ width: 750, height: '65vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }} onClick={e => e.stopPropagation()}>
                    <div className="adm-modal-header">
                        <h2>
                            <i className="codicon codicon-organization" style={{ marginRight: 8, color: '#3498db' }} />
                            {isEditing ? `Group Settings — ${groupName}` : 'Add New Trading Group'}
                        </h2>
                        <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                    </div>

                    <div className="adm-tabs" style={{ padding: '0 16px', borderBottom: '1px solid var(--theia-border)' }}>
                        {TABS.map(t => {
                            const err = tabHasErrors(t.id);
                            return (
                                <button 
                                    key={t.id} 
                                    type="button"
                                    className={`adm-tab ${activeTab === t.id ? 'active' : ''} ${err ? 'tab-error' : ''}`}
                                    onClick={() => setActiveTab(t.id)}
                                    style={{ position: 'relative' }}
                                >
                                    {t.label}
                                    {err && <span className="adm-tab-error-dot" />}
                                </button>
                            );
                        })}
                    </div>

                    <div className="adm-modal-body" style={{ flex: 1, overflow: 'hidden', padding: '12px 16px', display: 'flex', flexDirection: 'column' }}>
                        {loading && (
                            <div style={{ position: 'absolute', inset: 0, background: 'rgba(0,0,0,0.2)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 10 }}>
                                <span>Loading details...</span>
                            </div>
                        )}
                        
                        {saveError && (
                            <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 16px 0' }}>
                                <i className="codicon codicon-error" /> {saveError}
                            </div>
                        )}

                        {renderActiveTabContent()}
                    </div>

                    <div className="adm-modal-footer" style={{ borderTop: '1px solid var(--theia-border)' }}>
                        <button type="button" className="adm-btn adm-btn-primary" onClick={handleSave} disabled={loading}>
                            OK
                        </button>
                        <button type="button" className="adm-btn" onClick={onClose} disabled={loading}>
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </GroupDraftContext.Provider>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-commissionstab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/CommissionsTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft, CommissionRule } from '../GroupDraftContext';
import { CommissionRuleDialog } from './commissions/CommissionRuleDialog';

export function CommissionsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();
    const [selectedIdx, setSelectedIdx] = React.useState<number | null>(null);

    const [showDialog, setShowDialog] = React.useState(false);
    const [editRule, setEditRule] = React.useState<CommissionRule | null>(null);

    const handleAdd = () => {
        setEditRule(null);
        setShowDialog(true);
    };

    const handleEdit = () => {
        if (selectedIdx === null) return;
        setEditRule(draft.commission_rules[selectedIdx]);
        setShowDialog(true);
    };

    const handleDelete = () => {
        if (selectedIdx === null) return;
        setDraft(prev => ({
            ...prev,
            commission_rules: prev.commission_rules.filter((_, idx) => idx !== selectedIdx)
        }));
        setSelectedIdx(null);
    };

    const handleSaveRule = (rule: CommissionRule) => {
        setDraft(prev => {
            const nextRules = [...prev.commission_rules];
            if (editRule && selectedIdx !== null) {
                nextRules[selectedIdx] = rule;
            } else {
                nextRules.push(rule);
            }
            return { ...prev, commission_rules: nextRules };
        });
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e74c3c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    %
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure automated client deal commission rules, charging formulas, and target symbol pattern constraints.
                </div>
            </div>

            {/* Toolbar */}
            <div className="adm-toolbar" style={{ padding: '0px 0px 4px 0px', borderBottom: 'none', display: 'flex', gap: 6, flexShrink: 0 }}>
                <button type="button" className="adm-btn adm-btn-primary" style={{ padding: '2px 8px', height: 22, fontSize: 11 }} onClick={handleAdd}><i className="codicon codicon-add" /> Add Commission</button>
                <button type="button" className="adm-btn" style={{ padding: '2px 8px', height: 22, fontSize: 11 }} disabled={selectedIdx === null} onClick={handleEdit}><i className="codicon codicon-edit" /> Edit</button>
                <button type="button" className="adm-btn adm-btn-danger" style={{ padding: '2px 8px', height: 22, fontSize: 11 }} disabled={selectedIdx === null} onClick={handleDelete}><i className="codicon codicon-trash" /> Delete</button>
            </div>

            {/* Table Area */}
            <div className="adm-table-wrap" style={{ border: '1px solid var(--theia-border)', flex: 1, overflowY: 'auto' }}>
                <table className="adm-table" style={{ fontSize: 11 }}>
                    <thead>
                        <tr>
                            <th>Name</th>
                            <th>Symbols Pattern</th>
                            <th>Rate</th>
                            <th>Type</th>
                        </tr>
                    </thead>
                    <tbody>
                        {draft.commission_rules.length === 0 ? (
                            <tr>
                                <td colSpan={4} style={{ textAlign: 'center', opacity: 0.6, padding: 20 }}>
                                    No commissions configured for this group. Deals will run with zero charges.
                                </td>
                            </tr>
                        ) : (
                            draft.commission_rules.map((rule, idx) => (
                                <tr 
                                    key={idx} 
                                    className={selectedIdx === idx ? 'selected' : ''}
                                    onClick={() => setSelectedIdx(idx)}
                                    onDoubleClick={handleEdit}
                                    style={{ height: 22 }}
                                >
                                    <td><strong>{rule.name}</strong></td>
                                    <td><code>{rule.symbols}</code></td>
                                    <td>{rule.rate}</td>
                                    <td>
                                        <span className="adm-tag" style={{ padding: '1px 4px', fontSize: 9 }}>
                                            {rule.type === 'points' ? 'points' : rule.type === 'percent' ? 'percent' : 'money/lot'}
                                        </span>
                                    </td>
                                </tr>
                            ))
                        )}
                    </tbody>
                </table>
            </div>

            {showDialog && (
                <CommissionRuleDialog 
                    rule={editRule}
                    onClose={() => setShowDialog(false)}
                    onSave={handleSaveRule}
                />
            )}
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-commontab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/CommonTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const CURRENCIES = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'AUD', 'CAD'];
const AUTH_METHODS = ['Normal', '1024-bit RSA SSL', '2048-bit RSA SSL', 'Custom SSL certificate'];
const SERVERS = ['MetaQuotes-Demo', 'History-01', 'Access-01', 'Backup-01'];

export function CommonTab(): React.ReactElement {
    const { draft, setDraft, errors, setErrors } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
        
        // Validation logic
        setErrors(prev => {
            const next = { ...prev };
            if (field === 'name') {
                if (!val) {
                    next.name = 'Group name is required';
                } else if (/[/:*?"<>|]/.test(val)) {
                    next.name = 'Group name cannot contain special characters like /, :, *, ?, ", <, >, |';
                } else {
                    delete next.name;
                }
            }
            return next;
        });
    };

    // Auto digit lock for standard currencies
    React.useEffect(() => {
        if (CURRENCIES.includes(draft.currency)) {
            updateField('digits', 2);
        }
    }, [draft.currency]);

    const isDemoGroup = draft.name.toLowerCase().includes('demo');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#3498db', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    G
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure group identification, accounting deposit currency, connection servers, and security authentication parameters.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1 }}>
                
                {/* Left Column (General & Authentication) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        General & Authentication
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Name (path):</span>
                        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                            <input 
                                className={`adm-input ${errors.name ? 'error' : ''}`}
                                style={{ height: 20, padding: '2px 6px', fontSize: 11 }}
                                placeholder="e.g. demo\forex"
                                value={draft.name}
                                onChange={e => updateField('name', e.target.value)}
                            />
                            {errors.name && <span className="adm-input-error-text" style={{ fontSize: 9, color: 'var(--theia-errorForeground)' }}>{errors.name}</span>}
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Currency:</span>
                        <div style={{ flex: 1, display: 'flex', gap: 6 }}>
                            <select 
                                className="adm-select" 
                                style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                value={CURRENCIES.includes(draft.currency) ? draft.currency : 'other'}
                                onChange={e => {
                                    const val = e.target.value;
                                    if (val !== 'other') {
                                        updateField('currency', val);
                                    }
                                }}
                            >
                                {CURRENCIES.map(c => <option key={c} value={c}>{c}</option>)}
                                <option value="other">Custom...</option>
                            </select>
                            {!CURRENCIES.includes(draft.currency) && (
                                <input 
                                    className="adm-input" 
                                    style={{ width: 60, height: 20, padding: '2px 6px', fontSize: 11 }}
                                    placeholder="e.g. USD"
                                    value={draft.currency} 
                                    onChange={e => updateField('currency', e.target.value.toUpperCase())}
                                />
                            )}
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Digits:</span>
                        <input 
                            className="adm-input" 
                            type="number"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            disabled={CURRENCIES.includes(draft.currency)}
                            value={draft.digits}
                            onChange={e => updateField('digits', parseInt(e.target.value) || 0)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Trade Server:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.trade_server} onChange={e => updateField('trade_server', e.target.value)}>
                            {SERVERS.map(s => <option key={s} value={s}>{s}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Auth Mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.authentication} onChange={e => updateField('authentication', e.target.value)}>
                            {AUTH_METHODS.map(a => <option key={a} value={a}>{a}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Min Pass Len:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            max={16}
                            min={5}
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.min_password_len}
                            onChange={e => updateField('min_password_len', Math.min(16, parseInt(e.target.value) || 8))}
                        />
                    </div>
                </div>

                {/* Right Column (OTP & Regulatory Controls) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Security & Regulatory Options
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.enable_cert_confirm} onChange={e => updateField('enable_cert_confirm', e.target.checked)} />
                        Confirm client SSL certificates
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.change_pass_first_login} onChange={e => updateField('change_pass_first_login', e.target.checked)} />
                        Force password change first login
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.enable_connections} onChange={e => updateField('enable_connections', e.target.checked)} />
                        Enable group client connections
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.regulatory_restrictions} onChange={e => updateField('regulatory_restrictions', e.target.checked)} />
                        Enforce retail leverage restrictions (ESMA)
                    </label>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 70, textAlign: 'right', opacity: 0.8 }}>OTP Mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.otp_mode} onChange={e => updateField('otp_mode', e.target.value)}>
                            <option value="disabled">Disabled</option>
                            <option value="all">Required for all</option>
                            <option value="web">Required for Web Platform</option>
                        </select>
                    </div>

                    {draft.otp_mode !== 'disabled' && (
                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, paddingLeft: 10 }}>
                            <input type="checkbox" checked={draft.force_otp} onChange={e => updateField('force_otp', e.target.checked)} />
                            Force OTP registration window
                        </label>
                    )}

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: isDemoGroup ? 0.6 : 1 }}>
                        <input type="checkbox" disabled={isDemoGroup} checked={!isDemoGroup && draft.show_risk_warning} onChange={e => updateField('show_risk_warning', e.target.checked)} />
                        Show connection risk warnings
                    </label>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-companytab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/CompanyTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

export function CompanyTab(): React.ReactElement {
    const { draft, setDraft, errors, setErrors } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
        
        // Remove error if valid
        if (field === 'company' && val) {
            setErrors(prev => {
                const next = { ...prev };
                delete next.company;
                return next;
            });
        }
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#34495e', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    C
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure licensee business parameters, automated templates paths, client support portals, and website routing URLs.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Licensee info) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Licensee Credentials
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }} className="required">Company:</span>
                        <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                            <select 
                                className={`adm-select ${errors.company ? 'error' : ''}`}
                                style={{ height: 20, padding: '2px 6px', fontSize: 11 }}
                                value={draft.company}
                                onChange={e => updateField('company', e.target.value)}
                            >
                                <option value="">Select Company...</option>
                                <option value="MetaQuotes Software Corp.">MetaQuotes Software Corp.</option>
                                <option value="Demo Brokerage Ltd.">Demo Broker brokerage Ltd.</option>
                                <option value="Global Clearing Inc.">Global Clearing Inc.</option>
                            </select>
                            {errors.company && <span className="adm-input-error-text" style={{ fontSize: 9, color: 'var(--theia-errorForeground)' }}>{errors.company}</span>}
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Website URL:</span>
                        <input 
                            className="adm-input" 
                            type="url"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="https://www.company.com" 
                            value={draft.company_website} 
                            onChange={e => updateField('company_website', e.target.value)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Corporate Email:</span>
                        <input 
                            className="adm-input" 
                            type="email"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="info@company.com" 
                            value={draft.company_email} 
                            onChange={e => updateField('company_email', e.target.value)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Templates Dir:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="e.g. standard_templates" 
                            value={draft.templates_folder} 
                            onChange={e => updateField('templates_folder', e.target.value)} 
                        />
                    </div>
                </div>

                {/* Right Column (Web Portals & Support) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Client Support & Portals
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Deposit URL:</span>
                        <input 
                            className="adm-input" 
                            type="url"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="https://client.company.com/deposit" 
                            value={draft.deposit_url} 
                            onChange={e => updateField('deposit_url', e.target.value)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Withdrawal URL:</span>
                        <input 
                            className="adm-input" 
                            type="url"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="https://client.company.com/withdraw" 
                            value={draft.withdrawal_url} 
                            onChange={e => updateField('withdrawal_url', e.target.value)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Support URL:</span>
                        <input 
                            className="adm-input" 
                            type="url"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="https://support.company.com" 
                            value={draft.support_site} 
                            onChange={e => updateField('support_site', e.target.value)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Support Email:</span>
                        <input 
                            className="adm-input" 
                            type="email"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="support@company.com" 
                            value={draft.support_email} 
                            onChange={e => updateField('support_email', e.target.value)} 
                        />
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-gatewaytab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/GatewayTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';
import { API } from '../../../api';

export function GatewayTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();
    const [gateways, setGateways] = React.useState<any[]>([]);

    React.useEffect(() => {
        API.getGateways()
            .then((data: any) => {
                const filtered = data.filter((g: any) => !g.type.startsWith('Feeder_'));
                setGateways(filtered);
            })
            .catch(console.error);
    }, []);

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const selectedGateway = gateways.find(g => g.id === draft.gateway_id);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#3498db', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    G
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Define loopback interface routing servers settings for secure history/trading component tunnels.
                    Trading operations of this group will be routed to A-Book channels through the gateway selected below.
                </div>
            </div>

            {/* Form controls */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column - Selection & Server */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        ECN Route Assignment
                    </div>
                    
                    <div className="adm-form-row">
                        <label>Default A-Book Gateway</label>
                        <select 
                            className="adm-select" 
                            style={{ width: '100%', height: 20, padding: '2px 6px', fontSize: 11 }} 
                            value={draft.gateway_id || ''} 
                            onChange={e => updateField('gateway_id', e.target.value ? parseInt(e.target.value) : undefined)}
                        >
                            <option value="">None (B-Book Local Matching)</option>
                            {gateways.map(g => (
                                <option key={g.id} value={g.id}>
                                    {g.name} ({g.type})
                                </option>
                            ))}
                        </select>
                    </div>

                    <div className="adm-form-row">
                        <label>Gateway Server (IP:Port)</label>
                        <input 
                            className="adm-input" 
                            style={{ width: '100%', height: 20 }} 
                            disabled 
                            value={selectedGateway ? `${selectedGateway.host || 'localhost'}:${selectedGateway.port || '8003'}` : '—'} 
                        />
                    </div>
                </div>

                {/* Right Column - Authentication Details */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Gateway Authentication Details
                    </div>

                    <div className="adm-form-row">
                        <label>Gateway Login</label>
                        <input 
                            className="adm-input" 
                            style={{ width: '100%', height: 20 }} 
                            disabled 
                            value={selectedGateway ? (selectedGateway.username || 'Numeric Login') : '—'} 
                        />
                    </div>

                    <div className="adm-form-row">
                        <label>Gateway Password</label>
                        <input 
                            className="adm-input" 
                            type="password" 
                            style={{ width: '100%', height: 20 }} 
                            disabled 
                            value={selectedGateway ? '••••••••' : ''} 
                            placeholder={selectedGateway ? 'Loopback key' : '—'} 
                        />
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-margintab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/MarginTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const MODELS = [
    { value: 'netting', label: 'Retail Forex/CFD/Futures (netting)' },
    { value: 'hedging', label: 'Retail Forex/CFD/Futures with hedging' },
    { value: 'discount', label: 'Stock Exchange (margin discount rates)' }
];

const LEVERAGES = ['Default', 'Forex-Standard', 'CFD-HighRisk', 'MiniAccounts'];

export function MarginTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const isHedging = draft.risk_management_model === 'hedging';

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e67e22', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    M
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure group risk management calculations, margin stop out levels, stop out balance compensation, and floating leverage rules.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Risk Model & Levels) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Model & Margin Levels
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Risk Model:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.risk_management_model} onChange={e => updateField('risk_management_model', e.target.value)}>
                            {MODELS.map(m => <option key={m.value} value={m.value}>{m.label}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Calculation Base:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.stop_out_mode} onChange={e => updateField('stop_out_mode', e.target.value)}>
                            <option value="percent">In percent of margin level</option>
                            <option value="money">In absolute money value</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Margin Call:</span>
                        <div style={{ flex: 1, display: 'flex', alignItems: 'center', gap: 4 }}>
                            <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.margin_call} onChange={e => updateField('margin_call', parseFloat(e.target.value) || 0)} />
                            <span>{draft.stop_out_mode === 'percent' ? '%' : 'USD'}</span>
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Stop Out Level:</span>
                        <div style={{ flex: 1, display: 'flex', alignItems: 'center', gap: 4 }}>
                            <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.margin_stop_out} onChange={e => updateField('margin_stop_out', parseFloat(e.target.value) || 0)} />
                            <span>{draft.stop_out_mode === 'percent' ? '%' : 'USD'}</span>
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Leverage Profile:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.floating_leverage_profile} onChange={e => updateField('floating_leverage_profile', e.target.value)}>
                            {LEVERAGES.map(l => <option key={l} value={l}>{l}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Virtual Credit:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="0.00" value={draft.virtual_credit} onChange={e => updateField('virtual_credit', parseFloat(e.target.value) || 0)} />
                    </div>
                </div>

                {/* Right Column (Policies & Profit modes) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Stop Out Policy & Free Margin
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: isHedging ? 1 : 0.5 }}>
                        <input type="checkbox" disabled={!isHedging} checked={isHedging && draft.stop_out_hedged} onChange={e => updateField('stop_out_hedged', e.target.checked)} />
                        Stop out fully hedged accounts
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.compensate_negative_balance} onChange={e => updateField('compensate_negative_balance', e.target.checked)} />
                        Compensate negative balance automatically
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: draft.compensate_negative_balance ? 1 : 0.5 }}>
                        <input type="checkbox" disabled={!draft.compensate_negative_balance} checked={draft.compensate_negative_balance && draft.withdraw_credit_after_comp} onChange={e => updateField('withdraw_credit_after_comp', e.target.checked)} />
                        Withdraw virtual credit after compensation
                    </label>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Unrealized Profit:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.unrealized_profit_mode} onChange={e => updateField('unrealized_profit_mode', parseInt(e.target.value))}>
                            <option value={0}>Do not use unrealized profit/loss</option>
                            <option value={1}>Use both profit and loss</option>
                            <option value={2}>Use unrealized loss only</option>
                            <option value={3}>Use unrealized profit only</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Daily Profit:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.daily_fixed_profit_mode} onChange={e => updateField('daily_fixed_profit_mode', parseInt(e.target.value))}>
                            <option value={0}>Do not use daily fixed profit/loss</option>
                            <option value={1}>Use daily fixed profit/loss</option>
                        </select>
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: draft.daily_fixed_profit_mode === 1 ? 1 : 0.5, paddingLeft: 10 }}>
                        <input type="checkbox" disabled={draft.daily_fixed_profit_mode !== 1} checked={draft.daily_fixed_profit_mode === 1 && draft.release_fixed_profit} onChange={e => updateField('release_fixed_profit', e.target.checked)} />
                        Release fixed profit daily (netting)
                    </label>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-newsmailtab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/NewsMailTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const LANG_OPTIONS = [
    'Any language',
    'English',
    'German',
    'Chinese',
    'Russian',
    'Spanish',
    'French',
    'Arabic'
];

export function NewsMailTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const toggleLanguage = (lang: string) => {
        let nextLangs = [...draft.news_languages];
        if (lang === 'Any language') {
            nextLangs = ['Any language'];
        } else {
            // Remove 'Any language' if specific language is chosen
            nextLangs = nextLangs.filter(l => l !== 'Any language');
            if (nextLangs.includes(lang)) {
                nextLangs = nextLangs.filter(l => l !== lang);
            } else {
                nextLangs.push(lang);
            }
            if (nextLangs.length === 0) {
                nextLangs = ['Any language'];
            }
        }
        updateField('news_languages', nextLangs);
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#9b59b6', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    N
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure news categories, client terminal news distribution modes, language filters, and internal email availability.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (News Delivery & Mailbox) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        News & Messaging Settings
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>News Mode:</span>
                        <select 
                            className="adm-select"
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.news_mode}
                            onChange={e => updateField('news_mode', e.target.value)}
                        >
                            <option value="none">None</option>
                            <option value="headers">Headers Only</option>
                            <option value="full">Full Package</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>News Categories:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="e.g. Forex, Stocks\US" 
                            value={draft.news_categories}
                            onChange={e => updateField('news_categories', e.target.value)}
                        />
                    </div>

                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginTop: 8, marginBottom: 2 }}>
                        Mailbox Settings
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 8, cursor: 'pointer', height: 18 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.enable_internal_mail}
                            onChange={e => updateField('enable_internal_mail', e.target.checked)}
                        />
                        <span>Enable client mailbox in terminal</span>
                    </label>
                </div>

                {/* Right Column (News Languages list) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Language Filters
                    </div>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '6px 12px' }}>
                        {LANG_OPTIONS.map(lang => {
                            const isChecked = draft.news_languages.includes(lang);
                            return (
                                <label key={lang} style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', fontSize: 11 }}>
                                    <input 
                                        type="checkbox"
                                        checked={isChecked}
                                        onChange={() => toggleLanguage(lang)}
                                    />
                                    {lang}
                                </label>
                            );
                        })}
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-permissionstab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/PermissionsTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const SIGNALS_OPTIONS = [
    { value: 'disabled', label: 'Disabled' },
    { value: 'all', label: 'Enable all signals' },
    { value: 'own_only', label: 'From my servers only' }
];

const TRANSFER_OPTIONS = [
    { value: 'disabled', label: 'Disabled' },
    { value: 'same_details', label: 'Same name + email only' },
    { value: 'subgroup', label: 'Within same subgroup' },
    { value: 'subgroup_name', label: 'Same name in group' }
];

export function PermissionsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const isDemo = draft.name.toLowerCase().includes('demo');
    const isNetting = draft.risk_management_model === 'netting';

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e74c3c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    P
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure client permissions, algorithmic trading policies (EAs), maximum active order/position limits, and internal wallet funds transfers.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Limits & Demo specs) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Trading Limits & Finances
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max Symbols:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="0 = unlimited" value={draft.max_symbols} onChange={e => updateField('max_symbols', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max Positions:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="0 = unlimited" value={draft.max_positions} onChange={e => updateField('max_positions', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max Orders:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="0 = unlimited" value={draft.max_orders} onChange={e => updateField('max_orders', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>History Scope:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.available_history} onChange={e => updateField('available_history', e.target.value)}>
                            <option value="All">All history logs</option>
                            <option value="1 month">1 Month</option>
                            <option value="3 months">3 Months</option>
                            <option value="6 months">6 Months</option>
                            <option value="1 year">1 Year</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Interest Rate (%):</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="e.g. 2.50" value={draft.interest_rate} onChange={e => updateField('interest_rate', parseFloat(e.target.value) || 0)} />
                    </div>

                    {isDemo && (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Default Deposit:</span>
                                <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.default_deposit} onChange={e => updateField('default_deposit', parseInt(e.target.value) || 10000)} />
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Default Leverage:</span>
                                <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="1:100" value={draft.default_leverage} onChange={e => updateField('default_leverage', parseInt(e.target.value) || 100)} />
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Expiry days:</span>
                                <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="Inactivity limit" value={draft.inactivity_days} onChange={e => updateField('inactivity_days', parseInt(e.target.value) || 0)} />
                            </div>
                        </>
                    )}
                </div>

                {/* Right Column (Permissions & EAs) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Signals & Algorithm Policies
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Signals:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.trade_signals_mode} onChange={e => updateField('trade_signals_mode', e.target.value)}>
                            {SIGNALS_OPTIONS.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Transfers:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.transfer_funds_mode} onChange={e => updateField('transfer_funds_mode', e.target.value)}>
                            {TRANSFER_OPTIONS.map(o => <option key={o.value} value={o.value}>{o.label}</option>)}
                        </select>
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, marginTop: 4 }}>
                        <input type="checkbox" checked={draft.enable_swaps} onChange={e => updateField('enable_swaps', e.target.checked)} />
                        Enable swaps calculations and charging
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.enable_trailing_stops} onChange={e => updateField('enable_trailing_stops', e.target.checked)} />
                        Allow client terminal trailing stops
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.enable_ea_trading} onChange={e => updateField('enable_ea_trading', e.target.checked)} />
                        Allow Expert Advisor algorithmic trading
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: isNetting ? 1 : 0.5 }}>
                        <input type="checkbox" disabled={!isNetting} checked={isNetting && draft.fifo_rule} onChange={e => updateField('fifo_rule', e.target.checked)} />
                        Close positions strictly by FIFO rules
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: !isNetting ? 1 : 0.5 }}>
                        <input type="checkbox" disabled={isNetting} checked={!isNetting && draft.prohibit_hedge} onChange={e => updateField('prohibit_hedge', e.target.checked)} />
                        Prohibit hedge positions (hedging only)
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18 }}>
                        <input type="checkbox" checked={draft.deal_cost_calc} onChange={e => updateField('deal_cost_calc', e.target.checked)} />
                        Enable real-time deal cost calculation
                    </label>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-reportstab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/ReportsTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft } from '../GroupDraftContext';

const MAIL_SERVERS = ['Default', 'Local-Postfix', 'AWS-SES', 'SendGrid-SMTP'];

export function ReportsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const hasReports = draft.report_generation !== 'off';

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#1abc9c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    R
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure automated daily/monthly statement generation schedules, template output files, and email SMTP servers.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Statement & Ingestion) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Statement Generation
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Generate Data:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.report_generation} onChange={e => updateField('report_generation', e.target.value)}>
                            <option value="off">Off (No reports)</option>
                            <option value="daily">End of Day (Daily)</option>
                            <option value="monthly">End of Month (Monthly)</option>
                            <option value="both">Both Daily & Monthly</option>
                        </select>
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: hasReports ? 1 : 0.5, marginTop: 4 }}>
                        <input type="checkbox" disabled={!hasReports} checked={hasReports && draft.generate_statements} onChange={e => updateField('generate_statements', e.target.checked)} />
                        Generate HTML/PDF statements
                    </label>
                </div>

                {/* Right Column (SMTP Transmission) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Email Transmission Settings
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: hasReports && draft.generate_statements ? 1 : 0.5 }}>
                        <input type="checkbox" disabled={!hasReports || !draft.generate_statements} checked={hasReports && draft.generate_statements && draft.send_statements_email} onChange={e => updateField('send_statements_email', e.target.checked)} />
                        Send statements via email to clients
                    </label>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Mail Server:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} disabled={!draft.send_statements_email} value={draft.mail_server} onChange={e => updateField('mail_server', e.target.value)}>
                            {MAIL_SERVERS.map(m => <option key={m} value={m}>{m}</option>)}
                        </select>
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 18, opacity: draft.send_statements_email ? 1 : 0.5, marginTop: 4 }}>
                        <input type="checkbox" disabled={!draft.send_statements_email} checked={draft.send_statements_email && draft.send_copies_support} onChange={e => updateField('send_copies_support', e.target.checked)} />
                        Send copies to corporate support
                    </label>

                    {draft.send_copies_support && (
                        <div style={{ fontSize: 10, color: 'var(--theia-descriptionForeground)', paddingLeft: 20 }}>
                            To: <strong>{draft.support_email || '(No support email configured)'}</strong>
                        </div>
                    )}
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-symbolstab-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/SymbolsTab.tsx`

```tsx
import * as React from 'react';
import { useGroupDraft, SymbolRule } from '../GroupDraftContext';
import { SymbolRuleDialog } from './symbols/SymbolRuleDialog';
import { API } from '../../../api';

export function SymbolsTab(): React.ReactElement {
    const { draft, setDraft } = useGroupDraft();
    const [symbolsList, setSymbolsList] = React.useState<string[]>([]);
    const [selectedIdx, setSelectedIdx] = React.useState<number | null>(null);
    
    // Modal states
    const [showDialog, setShowDialog] = React.useState(false);
    const [editRule, setEditRule] = React.useState<SymbolRule | null>(null);

    const loadSymbols = async () => {
        try {
            const data = await API.getSymbols();
            setSymbolsList(data.map((s: any) => s.symbol));
        } catch (e) {
            console.error('Failed to load active symbols checklist:', e);
        }
    };

    React.useEffect(() => {
        loadSymbols();
    }, []);

    const handleAdd = () => {
        setEditRule(null);
        setShowDialog(true);
    };

    const handleEdit = () => {
        if (selectedIdx === null) return;
        setEditRule(draft.symbol_rules[selectedIdx]);
        setShowDialog(true);
    };

    const handleDelete = () => {
        if (selectedIdx === null) return;
        setDraft(prev => ({
            ...prev,
            symbol_rules: prev.symbol_rules.filter((_, idx) => idx !== selectedIdx)
        }));
        setSelectedIdx(null);
    };

    const handleSaveRule = (rule: SymbolRule) => {
        setDraft(prev => {
            const nextRules = [...prev.symbol_rules];
            if (editRule && selectedIdx !== null) {
                nextRules[selectedIdx] = rule;
            } else {
                nextRules.push(rule);
            }
            return { ...prev, symbol_rules: nextRules };
        });
    };

    // Helper to check if a strict symbol (no wildcard) exists in the database
    const checkSymbolExists = (pattern: string) => {
        if (pattern.includes('*') || pattern.includes('!')) return true; // pattern mask
        return symbolsList.includes(pattern);
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4, flexShrink: 0 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#2ecc71', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    S
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure financial instrument settings, trade permissions, overrides for spreads, commissions, and margin rates.
                </div>
            </div>

            {/* Layout Container: Action Buttons on Left, Table on Right */}
            <div style={{ display: 'flex', gap: 16, flex: 1, minHeight: 0 }}>
                {/* Action Buttons on Left */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8, width: 90, flexShrink: 0 }}>
                    <button 
                        type="button" 
                        className="adm-btn adm-btn-primary" 
                        onClick={handleAdd}
                        style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                    >
                        Add
                    </button>
                    <button 
                        type="button" 
                        className="adm-btn" 
                        disabled={selectedIdx === null} 
                        onClick={handleEdit}
                        style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                    >
                        Edit
                    </button>
                    <button 
                        type="button" 
                        className="adm-btn adm-btn-danger" 
                        disabled={selectedIdx === null} 
                        onClick={handleDelete}
                        style={{ fontSize: 11, width: '100%', height: 24, padding: '2px 8px' }}
                    >
                        Delete
                    </button>
                </div>

                {/* Table Area (Fills remaining container height with auto overflow) */}
                <div className="adm-table-wrap" style={{ border: '1px solid var(--theia-border)', flex: 1, overflowY: 'auto', height: '100%' }}>
                    <table className="adm-table" style={{ fontSize: 11 }}>
                        <thead>
                            <tr>
                                <th>Symbol Pattern</th>
                                <th>Trade Status</th>
                                <th>Spread Diff</th>
                                <th>Commission</th>
                                <th>Margin Multiplier</th>
                            </tr>
                        </thead>
                        <tbody>
                            {draft.symbol_rules.map((rule, idx) => {
                                const exists = checkSymbolExists(rule.symbol);
                                return (
                                    <tr 
                                        key={idx} 
                                        className={`${selectedIdx === idx ? 'selected' : ''} ${!exists ? 'adm-row-warning' : ''}`}
                                        onClick={() => setSelectedIdx(idx)}
                                        onDoubleClick={handleEdit}
                                        style={{ height: 22 }}
                                        title={!exists ? `Symbol "${rule.symbol}" does not exist in the active symbols database.` : ''}
                                    >
                                        <td>
                                            {!exists && <i className="codicon codicon-warning" style={{ color: '#f0ad4e', marginRight: 4 }} />}
                                            <strong>{rule.symbol}</strong>
                                        </td>
                                        <td>
                                            <span className={`adm-toggle ${rule.trade_allowed ? 'on' : 'off'}`} style={{ padding: '1px 4px', fontSize: 9 }}>
                                                {rule.trade_allowed ? '✓ ALLOW' : '✗ BLOCK'}
                                            </span>
                                        </td>
                                        <td>{rule.spread_diff > 0 ? `+${rule.spread_diff}` : rule.spread_diff} pts</td>
                                        <td>{rule.commission_rate} money</td>
                                        <td>{rule.margin_rate}x</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>

            {showDialog && (
                <SymbolRuleDialog 
                    rule={editRule}
                    availableSymbols={symbolsList}
                    onClose={() => setShowDialog(false)}
                    onSave={handleSaveRule}
                />
            )}
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-commissions-commissionruledialog-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/commissions/CommissionRuleDialog.tsx`

```tsx
import * as React from 'react';
import { CommissionRule } from '../../GroupDraftContext';

interface CommissionRuleDialogProps {
    rule: CommissionRule | null;
    onClose: () => void;
    onSave: (rule: CommissionRule) => void;
}

export function CommissionRuleDialog({ rule, onClose, onSave }: CommissionRuleDialogProps): React.ReactElement {
    const [name, setName] = React.useState(rule ? rule.name : '');
    const [symbols, setSymbols] = React.useState(rule ? rule.symbols : '*');
    const [rate, setRate] = React.useState(rule ? String(rule.rate) : '0.0');
    const [type, setType] = React.useState<any>(rule ? rule.type : 'money');
    const [error, setError] = React.useState<string | null>(null);

    const handleSave = (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        if (!name.trim()) {
            setError('Commission name is required.');
            return;
        }

        if (!symbols.trim()) {
            setError('Please define symbols pattern.');
            return;
        }

        onSave({
            name: name.trim(),
            symbols: symbols.trim(),
            rate: parseFloat(rate) || 0.0,
            type
        });
        onClose();
    };

    return (
        <div className="adm-modal-overlay" style={{ zIndex: 1100 }} onClick={onClose}>
            <form className="adm-modal" style={{ width: 360 }} onClick={e => e.stopPropagation()} onSubmit={handleSave}>
                <div className="adm-modal-header">
                    <h2>{rule ? 'Edit Commission Rule' : 'Add Commission Rule'}</h2>
                    <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                </div>
                <div className="adm-modal-body">
                    {error && (
                        <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 12px 0' }}>
                            <i className="codicon codicon-error" /> {error}
                        </div>
                    )}

                    <div className="adm-form-row">
                        <label className="required">Name</label>
                        <input className="adm-input" required placeholder="e.g. Standard Commission" value={name} onChange={e => setName(e.target.value)} />
                    </div>

                    <div className="adm-form-row">
                        <label className="required">Symbols Pattern</label>
                        <input className="adm-input" required placeholder="e.g. * or EURUSD" value={symbols} onChange={e => setSymbols(e.target.value)} />
                    </div>

                    <div className="adm-form-row">
                        <label>Commission Type</label>
                        <select className="adm-select" value={type} onChange={e => setType(e.target.value)}>
                            <option value="points">In points of spread</option>
                            <option value="percent">In percentage of deal volume</option>
                            <option value="money">In absolute money value per lot</option>
                        </select>
                    </div>

                    <div className="adm-form-row">
                        <label>Rate / Fee</label>
                        <input className="adm-input" type="number" step="0.001" value={rate} onChange={e => setRate(e.target.value)} />
                    </div>
                </div>
                <div className="adm-modal-footer">
                    <button type="submit" className="adm-btn adm-btn-primary">Save Commission</button>
                    <button type="button" className="adm-btn" onClick={onClose}>Cancel</button>
                </div>
            </form>
        </div>
    );
}

```

---

<a id='browser-modules-groups-modal-tabs-symbols-symbolruledialog-tsx'></a>
### 63. `browser/modules/groups/modal/tabs/symbols/SymbolRuleDialog.tsx`

```tsx
import * as React from 'react';
import { SymbolRule } from '../../GroupDraftContext';

interface SymbolRuleDialogProps {
    rule: SymbolRule | null;
    onClose: () => void;
    onSave: (rule: SymbolRule) => void;
    availableSymbols: string[];
}

type TabType = 'common' | 'trade' | 'execution' | 'margin' | 'rates' | 'swaps';

export function SymbolRuleDialog({ rule, onClose, onSave, availableSymbols }: SymbolRuleDialogProps): React.ReactElement {
    const [activeTab, setActiveTab] = React.useState<TabType>('common');
    const [error, setError] = React.useState<string | null>(null);

    // --- State declarations ---
    // Common Tab
    const [symbol, setSymbol] = React.useState(rule ? rule.symbol : '*');
    const [enableDom, setEnableDom] = React.useState(rule?.enable_dom ?? true);
    const [domLimit, setDomLimit] = React.useState(rule?.dom_limit ?? 'unlimited');
    const [useDefaultSpreads, setUseDefaultSpreads] = React.useState(rule?.use_default_spreads ?? true);
    const [spreadDiff, setSpreadDiff] = React.useState(rule ? String(rule.spread_diff) : '0');
    const [diffBalance, setDiffBalance] = React.useState(rule?.diff_balance ?? '1.5/1.5');
    const [useDefaultVolumes, setUseDefaultVolumes] = React.useState(rule?.use_default_volumes ?? true);
    const [volMin, setVolMin] = React.useState(rule ? String(rule.vol_min ?? 0.01) : '0.01');
    const [volStep, setVolStep] = React.useState(rule ? String(rule.vol_step ?? 0.01) : '0.01');
    const [volMax, setVolMax] = React.useState(rule ? String(rule.vol_max ?? 100.0) : '100.0');
    const [useDefaultLimit, setUseDefaultLimit] = React.useState(rule?.use_default_limit ?? true);
    const [volLimit, setVolLimit] = React.useState(rule ? String(rule.vol_limit ?? 0.0) : '0.0');

    // Trade Tab
    const [useDefaultTrade, setUseDefaultTrade] = React.useState(rule?.use_default_trade ?? true);
    const [tradeMode, setTradeMode] = React.useState(rule?.trade_mode ?? 'full'); // full, close, long, short, disabled
    const [fillingFok, setFillingFok] = React.useState(rule?.filling_fok ?? true);
    const [fillingIoc, setFillingIoc] = React.useState(rule?.filling_ioc ?? true);
    const [fillingBoc, setFillingBoc] = React.useState(rule?.filling_boc ?? false);
    const [expirationGtc, setExpirationGtc] = React.useState(rule?.expiration_gtc ?? true);
    const [expirationDay, setExpirationDay] = React.useState(rule?.expiration_day ?? true);
    const [expirationTime, setExpirationTime] = React.useState(rule?.expiration_time ?? false);
    const [expirationDate, setExpirationDate] = React.useState(rule?.expiration_date ?? false);
    const [useDefaultTradeLevels, setUseDefaultTradeLevels] = React.useState(rule?.use_default_trade_levels ?? true);
    const [limitStopLevel, setLimitStopLevel] = React.useState(rule ? String(rule.limit_stop_level ?? 0) : '0');
    const [freezeLevel, setFreezeLevel] = React.useState(rule ? String(rule.freeze_level ?? 0) : '0');

    // Execution Tab
    const [useDefaultExecution, setUseDefaultExecution] = React.useState(rule?.use_default_execution ?? true);
    const [execMode, setExecMode] = React.useState(rule?.exec_mode ?? 'market'); // instant, request, market, exchange
    const [instantMaxTimeDev, setInstantMaxTimeDev] = React.useState(rule ? String(rule.instant_max_time_dev ?? 0) : '0');
    const [instantMaxProfitDev, setInstantMaxProfitDev] = React.useState(rule ? String(rule.instant_max_profit_dev ?? 0) : '0');
    const [instantMaxLossDev, setInstantMaxLossDev] = React.useState(rule ? String(rule.instant_max_loss_dev ?? 0) : '0');
    const [instantMaxVolume, setInstantMaxVolume] = React.useState(rule ? String(rule.instant_max_volume ?? 0.0) : '0.0');
    const [requestTimeout, setRequestTimeout] = React.useState(rule ? String(rule.request_timeout ?? 0) : '0');
    const [requestConfirm, setRequestConfirm] = React.useState(rule?.request_confirm ?? false);

    // Margin Tab
    const [useDefaultMargin, setUseDefaultMargin] = React.useState(rule?.use_default_margin ?? true);
    const [initialMargin, setInitialMargin] = React.useState(rule ? String(rule.initial_margin ?? 0.0) : '0.0');
    const [maintenanceMargin, setMaintenanceMargin] = React.useState(rule ? String(rule.maintenance_margin ?? 0.0) : '0.0');
    const [hedgedMargin, setHedgedMargin] = React.useState(rule ? String(rule.hedged_margin ?? 0.0) : '0.0');
    const [calcHedgedLargerLeg, setCalcHedgedLargerLeg] = React.useState(rule?.calc_hedged_larger_leg ?? false);
    const [excludeLongPnl, setExcludeLongPnl] = React.useState(rule?.exclude_long_pnl ?? false);
    const [recalcMarginEod, setRecalcMarginEod] = React.useState(rule?.recalc_margin_eod ?? true);
    const [marginCheckExec, setMarginCheckExec] = React.useState(rule?.margin_check_exec ?? true);
    const [marginCheckSltp, setMarginCheckSltp] = React.useState(rule?.margin_check_sltp ?? false);

    // Margin Rates Tab
    const [useDefaultMarginRates, setUseDefaultMarginRates] = React.useState(rule?.use_default_margin_rates ?? true);
    const [liquidityRate, setLiquidityRate] = React.useState(rule ? String(rule.liquidity_rate ?? 0.0) : '0.0');
    const [currencyRate, setCurrencyRate] = React.useState(rule ? String(rule.currency_rate ?? 0.0) : '0.0');
    const [rateMarketBuy, setRateMarketBuy] = React.useState(rule ? String(rule.rate_market_buy ?? 1.0) : '1.0');
    const [rateMarketSell, setRateMarketSell] = React.useState(rule ? String(rule.rate_market_sell ?? 1.0) : '1.0');
    const [rateLimitBuy, setRateLimitBuy] = React.useState(rule ? String(rule.rate_limit_buy ?? 1.0) : '1.0');
    const [rateLimitSell, setRateLimitSell] = React.useState(rule ? String(rule.rate_limit_sell ?? 1.0) : '1.0');
    const [rateStopBuy, setRateStopBuy] = React.useState(rule ? String(rule.rate_stop_buy ?? 1.0) : '1.0');
    const [rateStopSell, setRateStopSell] = React.useState(rule ? String(rule.rate_stop_sell ?? 1.0) : '1.0');
    const [rateStopLimitBuy, setRateStopLimitBuy] = React.useState(rule ? String(rule.rate_stop_limit_buy ?? 1.0) : '1.0');
    const [rateStopLimitSell, setRateStopLimitSell] = React.useState(rule ? String(rule.rate_stop_limit_sell ?? 1.0) : '1.0');

    // Swaps Tab
    const [swapType, setSwapType] = React.useState(rule?.swap_type ?? 'disabled'); // disabled, points, percent, etc.
    const [swapLong, setSwapLong] = React.useState(rule ? String(rule.swap_long ?? 0.0) : '0.0');
    const [swapShort, setSwapShort] = React.useState(rule ? String(rule.swap_short ?? 0.0) : '0.0');
    const [swapDaysInYear, setSwapDaysInYear] = React.useState(rule?.swap_days_in_year ?? 360);
    const [swapMultMon, setSwapMultMon] = React.useState(rule ? String(rule.swap_multiplier_mon ?? 1) : '1');
    const [swapMultTue, setSwapMultTue] = React.useState(rule ? String(rule.swap_multiplier_tue ?? 1) : '1');
    const [swapMultWed, setSwapMultWed] = React.useState(rule ? String(rule.swap_multiplier_wed ?? 3) : '3');
    const [swapMultThu, setSwapMultThu] = React.useState(rule ? String(rule.swap_multiplier_thu ?? 1) : '1');
    const [swapMultFri, setSwapMultFri] = React.useState(rule ? String(rule.swap_multiplier_fri ?? 1) : '1');
    const [swapMultSat, setSwapMultSat] = React.useState(rule ? String(rule.swap_multiplier_sat ?? 0) : '0');
    const [swapMultSun, setSwapMultSun] = React.useState(rule ? String(rule.swap_multiplier_sun ?? 0) : '0');
    const [swapConsiderHolidays, setSwapConsiderHolidays] = React.useState(rule?.swap_consider_holidays ?? true);

    const [commissionRate, setCommissionRate] = React.useState(rule ? String(rule.commission_rate) : '0.0');
    const [marginRate, setMarginRate] = React.useState(rule ? String(rule.margin_rate) : '1.0');

    const handleSave = (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);

        // Validation
        const trimmed = symbol.trim();
        if (!trimmed) {
            setError('Symbol pattern cannot be empty.');
            setActiveTab('common');
            return;
        }

        const parts = trimmed.split(',').map(s => s.trim()).filter(Boolean);
        if (parts.length === 0) {
            setError('Please specify at least one valid symbol or mask.');
            setActiveTab('common');
            return;
        }

        const hasPositive = parts.some(p => !p.startsWith('!'));
        if (!hasPositive) {
            setError('Rules cannot contain only exclusions (!). At least one positive mask or symbol must be defined.');
            setActiveTab('common');
            return;
        }

        onSave({
            symbol: trimmed,
            trade_allowed: useDefaultTrade ? true : (tradeMode !== 'disabled'),
            spread_diff: useDefaultSpreads ? 0 : (parseInt(spreadDiff) || 0),
            commission_rate: parseFloat(commissionRate) || 0.0,
            margin_rate: parseFloat(marginRate) || 1.0,

            // Save Tab Details
            enable_dom: enableDom,
            dom_limit: domLimit,
            use_default_spreads: useDefaultSpreads,
            diff_balance: diffBalance,
            use_default_volumes: useDefaultVolumes,
            vol_min: parseFloat(volMin) || 0.01,
            vol_step: parseFloat(volStep) || 0.01,
            vol_max: parseFloat(volMax) || 100.0,
            use_default_limit: useDefaultLimit,
            vol_limit: parseFloat(volLimit) || 0.0,

            use_default_trade: useDefaultTrade,
            trade_mode: tradeMode,
            filling_fok: fillingFok,
            filling_ioc: fillingIoc,
            filling_boc: fillingBoc,
            expiration_gtc: expirationGtc,
            expiration_day: expirationDay,
            expiration_time: expirationTime,
            expiration_date: expirationDate,
            use_default_trade_levels: useDefaultTradeLevels,
            limit_stop_level: parseInt(limitStopLevel) || 0,
            freeze_level: parseInt(freezeLevel) || 0,

            use_default_execution: useDefaultExecution,
            exec_mode: execMode,
            instant_max_time_dev: parseInt(instantMaxTimeDev) || 0,
            instant_max_profit_dev: parseInt(instantMaxProfitDev) || 0,
            instant_max_loss_dev: parseInt(instantMaxLossDev) || 0,
            instant_max_volume: parseFloat(instantMaxVolume) || 0.0,
            request_timeout: parseInt(requestTimeout) || 0,
            request_confirm: requestConfirm,

            use_default_margin: useDefaultMargin,
            initial_margin: parseFloat(initialMargin) || 0.0,
            maintenance_margin: parseFloat(maintenanceMargin) || 0.0,
            hedged_margin: parseFloat(hedgedMargin) || 0.0,
            calc_hedged_larger_leg: calcHedgedLargerLeg,
            exclude_long_pnl: excludeLongPnl,
            recalc_margin_eod: recalcMarginEod,
            margin_check_exec: marginCheckExec,
            margin_check_sltp: marginCheckSltp,

            use_default_margin_rates: useDefaultMarginRates,
            liquidity_rate: parseFloat(liquidityRate) || 0.0,
            currency_rate: parseFloat(currencyRate) || 0.0,
            rate_market_buy: parseFloat(rateMarketBuy) || 1.0,
            rate_market_sell: parseFloat(rateMarketSell) || 1.0,
            rate_limit_buy: parseFloat(rateLimitBuy) || 1.0,
            rate_limit_sell: parseFloat(rateLimitSell) || 1.0,
            rate_stop_buy: parseFloat(rateStopBuy) || 1.0,
            rate_stop_sell: parseFloat(rateStopSell) || 1.0,
            rate_stop_limit_buy: parseFloat(rateStopLimitBuy) || 1.0,
            rate_stop_limit_sell: parseFloat(rateStopLimitSell) || 1.0,

            swap_type: swapType,
            swap_long: parseFloat(swapLong) || 0.0,
            swap_short: parseFloat(swapShort) || 0.0,
            swap_days_in_year: swapDaysInYear,
            swap_multiplier_mon: parseInt(swapMultMon) || 1,
            swap_multiplier_tue: parseInt(swapMultTue) || 1,
            swap_multiplier_wed: parseInt(swapMultWed) || 3,
            swap_multiplier_thu: parseInt(swapMultThu) || 1,
            swap_multiplier_fri: parseInt(swapMultFri) || 1,
            swap_multiplier_sat: parseInt(swapMultSat) || 0,
            swap_multiplier_sun: parseInt(swapMultSun) || 0,
            swap_consider_holidays: swapConsiderHolidays
        });
        onClose();
    };

    const handleApplyForexSwaps = () => {
        setSwapMultMon('1');
        setSwapMultTue('1');
        setSwapMultWed('3');
        setSwapMultThu('1');
        setSwapMultFri('1');
        setSwapMultSat('0');
        setSwapMultSun('0');
    };

    const handleApplyAllWeekSwaps = () => {
        setSwapMultMon('1');
        setSwapMultTue('1');
        setSwapMultWed('1');
        setSwapMultThu('1');
        setSwapMultFri('1');
        setSwapMultSat('1');
        setSwapMultSun('1');
    };

    return (
        <div className="adm-modal-overlay" style={{ zIndex: 1100 }} onClick={onClose}>
            <form className="adm-modal" style={{ width: 550, height: 500, display: 'flex', flexDirection: 'column' }} onClick={e => e.stopPropagation()} onSubmit={handleSave}>
                <div className="adm-modal-header" style={{ flexShrink: 0 }}>
                    <h2>{rule ? 'Edit Symbol Access Rule' : 'Add Symbol Access Rule'}</h2>
                    <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                </div>

                {/* Sub Tab Navigation */}
                <div style={{ display: 'flex', background: 'var(--theia-editor-background)', borderBottom: '1px solid var(--theia-border)', padding: '0 12px', gap: 8, flexShrink: 0 }}>
                    {(['common', 'trade', 'execution', 'margin', 'rates', 'swaps'] as TabType[]).map((tab) => (
                        <button
                            key={tab}
                            type="button"
                            className={`adm-tab ${activeTab === tab ? 'active' : ''}`}
                            onClick={() => setActiveTab(tab)}
                            style={{
                                border: 'none',
                                background: 'transparent',
                                padding: '8px 12px',
                                fontSize: 11,
                                cursor: 'pointer',
                                textTransform: 'capitalize',
                                borderBottom: activeTab === tab ? '2px solid var(--theia-accentColor, #3498db)' : '2px solid transparent',
                                color: activeTab === tab ? 'var(--theia-foreground)' : 'var(--theia-descriptionForeground)'
                            }}
                        >
                            {tab === 'rates' ? 'Margin Rates' : tab}
                        </button>
                    ))}
                </div>

                <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', padding: 16 }}>
                    {error && (
                        <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 12px 0' }}>
                            <i className="codicon codicon-error" /> {error}
                        </div>
                    )}

                    {/* --- COMMON TAB CONTENT --- */}
                    {activeTab === 'common' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label className="required">Symbol / Mask</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column' }}>
                                    <input 
                                        className="adm-input" 
                                        required
                                        placeholder="e.g. * or EURUSD or !GBPUSD" 
                                        value={symbol} 
                                        onChange={e => setSymbol(e.target.value)} 
                                    />
                                    <span className="adm-field-desc">Use <code>*</code> for wildcard, <code>!</code> to exclude (e.g. <code>*,!BTCUSD</code>).</span>
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Market Depth</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={enableDom} onChange={e => setEnableDom(e.target.checked)} />
                                        <span>Enable depth of market</span>
                                    </label>
                                    <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                        <span style={{ fontSize: 11, opacity: 0.8 }}>Depth limit:</span>
                                        <input className="adm-input" style={{ width: 80 }} value={domLimit} onChange={e => setDomLimit(e.target.value)} />
                                    </div>
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Spreads</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={useDefaultSpreads} onChange={e => setUseDefaultSpreads(e.target.checked)} />
                                        <span>Use default spreads</span>
                                    </label>
                                    {!useDefaultSpreads && (
                                        <div style={{ display: 'flex', gap: 12 }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                <span style={{ fontSize: 11, opacity: 0.8 }}>Spread Diff:</span>
                                                <input className="adm-input" style={{ width: 60 }} type="number" value={spreadDiff} onChange={e => setSpreadDiff(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                                <span style={{ fontSize: 11, opacity: 0.8 }}>Balance (Bid/Ask):</span>
                                                <input className="adm-input" style={{ width: 80 }} value={diffBalance} onChange={e => setDiffBalance(e.target.value)} />
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Order Volumes</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={useDefaultVolumes} onChange={e => setUseDefaultVolumes(e.target.checked)} />
                                        <span>Use default volumes</span>
                                    </label>
                                    {!useDefaultVolumes && (
                                        <div style={{ display: 'flex', gap: 8, flexWrap: 'wrap' }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                                <span style={{ fontSize: 10 }}>Min:</span>
                                                <input className="adm-input" style={{ width: 50 }} type="number" step="0.01" value={volMin} onChange={e => setVolMin(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                                <span style={{ fontSize: 10 }}>Step:</span>
                                                <input className="adm-input" style={{ width: 50 }} type="number" step="0.01" value={volStep} onChange={e => setVolStep(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                                <span style={{ fontSize: 10 }}>Max:</span>
                                                <input className="adm-input" style={{ width: 60 }} type="number" step="0.1" value={volMax} onChange={e => setVolMax(e.target.value)} />
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Position Limit</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={useDefaultLimit} onChange={e => setUseDefaultLimit(e.target.checked)} />
                                        <span>Use default limit</span>
                                    </label>
                                    {!useDefaultLimit && (
                                        <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                                            <span style={{ fontSize: 11, opacity: 0.8 }}>Limit:</span>
                                            <input className="adm-input" style={{ width: 80 }} type="number" step="0.1" value={volLimit} onChange={e => setVolLimit(e.target.value)} />
                                            <span style={{ fontSize: 10, opacity: 0.7 }}>lots</span>
                                        </div>
                                    )}
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Commission (rate)</label>
                                <input className="adm-input" type="number" step="0.0001" value={commissionRate} onChange={e => setCommissionRate(e.target.value)} />
                            </div>
                        </div>
                    )}

                    {/* --- TRADE TAB CONTENT --- */}
                    {activeTab === 'trade' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label>Trade Settings</label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                    <input type="checkbox" checked={useDefaultTrade} onChange={e => setUseDefaultTrade(e.target.checked)} />
                                    <span>Use default trade settings</span>
                                </label>
                            </div>

                            {!useDefaultTrade && (
                                <div className="adm-form-row">
                                    <label>Trade Permission</label>
                                    <select className="adm-input" value={tradeMode} onChange={e => setTradeMode(e.target.value)}>
                                        <option value="full">Full Access</option>
                                        <option value="close">Close Only</option>
                                        <option value="long">Long Only</option>
                                        <option value="short">Short Only</option>
                                        <option value="disabled">Disabled</option>
                                    </select>
                                </div>
                            )}

                            <div className="adm-form-row">
                                <label>Filling Policies</label>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={fillingFok} onChange={e => setFillingFok(e.target.checked)} />
                                        <span>Fill or Kill (FOK)</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={fillingIoc} onChange={e => setFillingIoc(e.target.checked)} />
                                        <span>Immediate or Cancel (IOC)</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={fillingBoc} onChange={e => setFillingBoc(e.target.checked)} />
                                        <span>Book or Cancel (BOC)</span>
                                    </label>
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Expiration Mode</label>
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={expirationGtc} onChange={e => setExpirationGtc(e.target.checked)} />
                                        <span>Good till canceled (GTC)</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={expirationDay} onChange={e => setExpirationDay(e.target.checked)} />
                                        <span>Day order</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={expirationTime} onChange={e => setExpirationTime(e.target.checked)} />
                                        <span>Specified time</span>
                                    </label>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={expirationDate} onChange={e => setExpirationDate(e.target.checked)} />
                                        <span>Specified day</span>
                                    </label>
                                </div>
                            </div>

                            <div className="adm-form-row">
                                <label>Trade Levels</label>
                                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                        <input type="checkbox" checked={useDefaultTradeLevels} onChange={e => setUseDefaultTradeLevels(e.target.checked)} />
                                        <span>Use default level settings</span>
                                    </label>
                                    {!useDefaultTradeLevels && (
                                        <div style={{ display: 'flex', gap: 12 }}>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                                <span style={{ fontSize: 11 }}>Stops:</span>
                                                <input className="adm-input" style={{ width: 60 }} type="number" value={limitStopLevel} onChange={e => setLimitStopLevel(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', alignItems: 'center', gap: 4 }}>
                                                <span style={{ fontSize: 11 }}>Freeze:</span>
                                                <input className="adm-input" style={{ width: 60 }} type="number" value={freezeLevel} onChange={e => setFreezeLevel(e.target.value)} />
                                            </div>
                                        </div>
                                    )}
                                </div>
                            </div>
                        </div>
                    )}

                    {/* --- EXECUTION TAB CONTENT --- */}
                    {activeTab === 'execution' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label>Execution Settings</label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                    <input type="checkbox" checked={useDefaultExecution} onChange={e => setUseDefaultExecution(e.target.checked)} />
                                    <span>Use default execution settings</span>
                                </label>
                            </div>

                            {!useDefaultExecution && (
                                <>
                                    <div className="adm-form-row">
                                        <label>Execution Mode</label>
                                        <select className="adm-input" value={execMode} onChange={e => setExecMode(e.target.value)}>
                                            <option value="instant">Instant Execution</option>
                                            <option value="request">Request Execution</option>
                                            <option value="market">Market Execution</option>
                                            <option value="exchange">Exchange Execution</option>
                                        </select>
                                    </div>

                                    {execMode === 'instant' && (
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, paddingLeft: 12, borderLeft: '2px solid var(--theia-border)' }}>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Max time dev (s):</span>
                                                <input className="adm-input" style={{ width: 80 }} type="number" value={instantMaxTimeDev} onChange={e => setInstantMaxTimeDev(e.target.value)} />
                                            </div>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Max profit dev:</span>
                                                <input className="adm-input" style={{ width: 80 }} type="number" value={instantMaxProfitDev} onChange={e => setInstantMaxProfitDev(e.target.value)} />
                                            </div>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Max losing dev:</span>
                                                <input className="adm-input" style={{ width: 80 }} type="number" value={instantMaxLossDev} onChange={e => setInstantMaxLossDev(e.target.value)} />
                                            </div>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Max volume (lots):</span>
                                                <input className="adm-input" style={{ width: 80 }} type="number" step="0.1" value={instantMaxVolume} onChange={e => setInstantMaxVolume(e.target.value)} />
                                            </div>
                                        </div>
                                    )}

                                    {execMode === 'request' && (
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 8, paddingLeft: 12, borderLeft: '2px solid var(--theia-border)' }}>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Timeout (s):</span>
                                                <input className="adm-input" style={{ width: 80 }} type="number" value={requestTimeout} onChange={e => setRequestTimeout(e.target.value)} />
                                            </div>
                                            <div className="adm-form-row">
                                                <span style={{ width: 120, fontSize: 11 }}>Confirm orders:</span>
                                                <input type="checkbox" checked={requestConfirm} onChange={e => setRequestConfirm(e.target.checked)} />
                                            </div>
                                        </div>
                                    )}
                                </>
                            )}
                        </div>
                    )}

                    {/* --- MARGIN TAB CONTENT --- */}
                    {activeTab === 'margin' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label>Margin Settings</label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                    <input type="checkbox" checked={useDefaultMargin} onChange={e => setUseDefaultMargin(e.target.checked)} />
                                    <span>Use default margin settings</span>
                                </label>
                            </div>

                            {!useDefaultMargin && (
                                <>
                                    <div className="adm-form-row">
                                        <label>Initial Margin</label>
                                        <input className="adm-input" type="number" step="0.1" value={initialMargin} onChange={e => setInitialMargin(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Maintenance Margin</label>
                                        <input className="adm-input" type="number" step="0.1" value={maintenanceMargin} onChange={e => setMaintenanceMargin(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Hedged Margin</label>
                                        <input className="adm-input" type="number" step="0.1" value={hedgedMargin} onChange={e => setHedgedMargin(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Hedged Mode</label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                            <input type="checkbox" checked={calcHedgedLargerLeg} onChange={e => setCalcHedgedLargerLeg(e.target.checked)} />
                                            <span>Calculate hedged margin using larger leg</span>
                                        </label>
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Free Margin Rules</label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                            <input type="checkbox" checked={excludeLongPnl} onChange={e => setExcludeLongPnl(e.target.checked)} />
                                            <span>Exclude long position PnL</span>
                                        </label>
                                    </div>
                                    <div className="adm-form-row">
                                        <label>End of Day</label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                            <input type="checkbox" checked={recalcMarginEod} onChange={e => setRecalcMarginEod(e.target.checked)} />
                                            <span>Recalculate margin exchange rate at EOD</span>
                                        </label>
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Additional Checks</label>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
                                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                                <input type="checkbox" checked={marginCheckExec} onChange={e => setMarginCheckExec(e.target.checked)} />
                                                <span>Check before executing orders</span>
                                            </label>
                                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                                <input type="checkbox" checked={marginCheckSltp} onChange={e => setMarginCheckSltp(e.target.checked)} />
                                                <span>Check on SL-TP trigger</span>
                                            </label>
                                        </div>
                                    </div>
                                </>
                            )}

                            <div className="adm-form-row">
                                <label>Margin Multiplier</label>
                                <input className="adm-input" type="number" step="0.1" value={marginRate} onChange={e => setMarginRate(e.target.value)} />
                            </div>
                        </div>
                    )}

                    {/* --- MARGIN RATES TAB CONTENT --- */}
                    {activeTab === 'rates' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label>Margin Rates</label>
                                <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                    <input type="checkbox" checked={useDefaultMarginRates} onChange={e => setUseDefaultMarginRates(e.target.checked)} />
                                    <span>Use default margin rate settings</span>
                                </label>
                            </div>

                            {!useDefaultMarginRates && (
                                <>
                                    <div className="adm-form-row">
                                        <label>Liquidity Rate</label>
                                        <input className="adm-input" type="number" step="0.1" value={liquidityRate} onChange={e => setLiquidityRate(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Currency Rate</label>
                                        <input className="adm-input" type="number" step="0.1" value={currencyRate} onChange={e => setCurrencyRate(e.target.value)} />
                                    </div>

                                    {/* Sub-grid of multipliers */}
                                    <div style={{ background: 'var(--theia-sideBarSectionHeader-background)', padding: 8, borderRadius: 4 }}>
                                        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 4, marginBottom: 6 }}>
                                            <span>Order Type</span>
                                            <span>Initial</span>
                                            <span>Maintenance</span>
                                        </div>
                                        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Market Buy</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateMarketBuy} onChange={e => setRateMarketBuy(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Market Sell</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateMarketSell} onChange={e => setRateMarketSell(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Buy Limit</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateLimitBuy} onChange={e => setRateLimitBuy(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Sell Limit</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateLimitSell} onChange={e => setRateLimitSell(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Buy Stop</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateStopBuy} onChange={e => setRateStopBuy(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Sell Stop</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateStopSell} onChange={e => setRateStopSell(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Buy Stop Limit</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateStopLimitBuy} onChange={e => setRateStopLimitBuy(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 6, alignItems: 'center' }}>
                                                <span style={{ fontSize: 10 }}>Sell Stop Limit</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" step="0.1" value={rateStopLimitSell} onChange={e => setRateStopLimitSell(e.target.value)} />
                                                <span style={{ fontSize: 9, opacity: 0.7 }}>Same</span>
                                            </div>
                                        </div>
                                    </div>
                                </>
                            )}
                        </div>
                    )}

                    {/* --- SWAPS TAB CONTENT --- */}
                    {activeTab === 'swaps' && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label>Swap Type</label>
                                <select className="adm-input" value={swapType} onChange={e => setSwapType(e.target.value)}>
                                    <option value="disabled">Disabled</option>
                                    <option value="points">Points</option>
                                    <option value="percent">Percentage</option>
                                    <option value="interest">Interest Rate</option>
                                </select>
                            </div>

                            {swapType !== 'disabled' && (
                                <>
                                    <div className="adm-form-row">
                                        <label>Long Positions</label>
                                        <input className="adm-input" type="number" step="0.01" value={swapLong} onChange={e => setSwapLong(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Short Positions</label>
                                        <input className="adm-input" type="number" step="0.01" value={swapShort} onChange={e => setSwapShort(e.target.value)} />
                                    </div>
                                    <div className="adm-form-row">
                                        <label>Days in Year</label>
                                        <select className="adm-input" value={swapDaysInYear} onChange={e => setSwapDaysInYear(parseInt(e.target.value))}>
                                            <option value={360}>360 days</option>
                                            <option value={365}>365 days</option>
                                            <option value={366}>366 days</option>
                                        </select>
                                    </div>

                                    {/* Multipliers per day */}
                                    <div style={{ background: 'var(--theia-sideBarSectionHeader-background)', padding: 8, borderRadius: 4 }}>
                                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--theia-border)', paddingBottom: 4, marginBottom: 8 }}>
                                            <span style={{ fontWeight: 'bold', fontSize: 10 }}>Swap Multipliers</span>
                                            <div style={{ display: 'flex', gap: 4 }}>
                                                <button type="button" className="adm-btn" style={{ fontSize: 9, padding: '1px 4px', height: 16 }} onClick={handleApplyForexSwaps}>Forex</button>
                                                <button type="button" className="adm-btn" style={{ fontSize: 9, padding: '1px 4px', height: 16 }} onClick={handleApplyAllWeekSwaps}>All Week</button>
                                            </div>
                                        </div>
                                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 6 }}>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Mon</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultMon} onChange={e => setSwapMultMon(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Tue</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultTue} onChange={e => setSwapMultTue(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Wed</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultWed} onChange={e => setSwapMultWed(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Thu</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultThu} onChange={e => setSwapMultThu(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Fri</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultFri} onChange={e => setSwapMultFri(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Sat</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultSat} onChange={e => setSwapMultSat(e.target.value)} />
                                            </div>
                                            <div style={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
                                                <span style={{ fontSize: 9 }}>Sun</span>
                                                <input className="adm-input" style={{ height: 18, fontSize: 10 }} type="number" value={swapMultSun} onChange={e => setSwapMultSun(e.target.value)} />
                                            </div>
                                        </div>
                                    </div>

                                    <div className="adm-form-row" style={{ marginTop: 8 }}>
                                        <label>Holidays</label>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', flex: 1 }}>
                                            <input type="checkbox" checked={swapConsiderHolidays} onChange={e => setSwapConsiderHolidays(e.target.checked)} />
                                            <span>Consider holidays in swap charging</span>
                                        </label>
                                    </div>
                                </>
                            )}
                        </div>
                    )}
                </div>

                <div className="adm-modal-footer" style={{ flexShrink: 0 }}>
                    <button type="submit" className="adm-btn adm-btn-primary">Save Rule</button>
                    <button type="button" className="adm-btn" onClick={onClose}>Cancel</button>
                </div>
            </form>
        </div>
    );
}

```

---

<a id='browser-modules-market-watch-marketwatchpage-tsx'></a>
### 63. `browser/modules/market-watch/MarketWatchPage.tsx`

```tsx
import * as React from 'react';
import { API } from '../api';

interface QuoteRow {
    symbol: string;
    bid: number;
    ask: number;
    age: number;
    spread: number;
    prevBid?: number;
    prevAsk?: number;
    flashBid?: 'up' | 'down';
    flashAsk?: 'up' | 'down';
}

function formatPrice(v: number): string {
    if (v >= 10000) return v.toFixed(2);
    if (v >= 100)   return v.toFixed(3);
    return v.toFixed(5);
}

function formatAge(s: number): string {
    if (s < 1) return '<1s';
    if (s < 60) return `${Math.round(s)}s`;
    if (s < 3600) return `${Math.floor(s / 60)}m ${Math.round(s % 60)}s`;
    return `${Math.floor(s / 3600)}h`;
}

function ageColor(age: number): string {
    if (age < 5) return 'var(--theia-successForeground, #2ecc71)';
    if (age < 30) return 'var(--theia-warningForeground, #f1c40f)';
    return 'var(--theia-errorForeground, #e74c3c)';
}

export function MarketWatchPage(): React.ReactElement {
    const [quotes, setQuotes] = React.useState<QuoteRow[]>([]);
    const [error, setError] = React.useState<string | null>(null);
    const [lastUpdate, setLastUpdate] = React.useState<Date | null>(null);
    const [filter, setFilter] = React.useState('');
    const prevRef = React.useRef<Record<string, { bid: number; ask: number }>>({});
    const flashTimers = React.useRef<Record<string, ReturnType<typeof setTimeout>>>({});

    const fetchQuotes = React.useCallback(async () => {
        try {
            const data = await API.getTicks();
            setError(null);
            setLastUpdate(new Date());

            setQuotes(prev => {
                const prevMap: Record<string, QuoteRow> = {};
                prev.forEach(r => { prevMap[r.symbol] = r; });

                const rows: QuoteRow[] = Object.entries(data)
                    .filter(([_, q]) => q.age <= 60)
                    .map(([symbol, q]) => {
                        const old = prevRef.current[symbol];
                        let flashBid: 'up' | 'down' | undefined;
                        let flashAsk: 'up' | 'down' | undefined;

                        if (old) {
                            if (q.bid > old.bid) flashBid = 'up';
                            else if (q.bid < old.bid) flashBid = 'down';
                            if (q.ask > old.ask) flashAsk = 'up';
                            else if (q.ask < old.ask) flashAsk = 'down';
                        }

                        prevRef.current[symbol] = { bid: q.bid, ask: q.ask };

                        return {
                            symbol,
                            bid: q.bid,
                            ask: q.ask,
                            age: q.age,
                            spread: Math.round((q.ask - q.bid) * 100000) / 10,
                            prevBid: old?.bid,
                            prevAsk: old?.ask,
                            flashBid,
                            flashAsk,
                        };
                    })
                    .sort((a, b) => a.symbol.localeCompare(b.symbol));

                return rows;
            });
        } catch (e: any) {
            setError(e?.message || 'Failed to fetch quotes');
        }
    }, []);

    React.useEffect(() => {
        fetchQuotes();
        const iv = setInterval(fetchQuotes, 1000);
        return () => clearInterval(iv);
    }, [fetchQuotes]);

    // Clear flash state after 400ms
    React.useEffect(() => {
        quotes.forEach(row => {
            if (row.flashBid || row.flashAsk) {
                if (flashTimers.current[row.symbol]) clearTimeout(flashTimers.current[row.symbol]);
                flashTimers.current[row.symbol] = setTimeout(() => {
                    setQuotes(prev => prev.map(r =>
                        r.symbol === row.symbol ? { ...r, flashBid: undefined, flashAsk: undefined } : r
                    ));
                }, 400);
            }
        });
    }, [quotes]);

    const filtered = filter.trim()
        ? quotes.filter(r => r.symbol.toLowerCase().includes(filter.toLowerCase()))
        : quotes;

    const connected = quotes.length > 0 && quotes.some(r => r.age < 30);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            {/* Header bar */}
            <div style={{
                display: 'flex', alignItems: 'center', gap: 12, padding: '8px 12px',
                borderBottom: '1px solid var(--theia-panel-border)',
                background: 'var(--theia-editor-background)',
                flexShrink: 0
            }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 6 }}>
                    <span style={{
                        width: 8, height: 8, borderRadius: '50%', display: 'inline-block',
                        background: connected ? '#2ecc71' : (error ? '#e74c3c' : '#95a5a6'),
                        boxShadow: connected ? '0 0 6px #2ecc7188' : 'none',
                        animation: connected ? 'pulse 2s infinite' : 'none'
                    }} />
                    <span style={{ fontWeight: 600, fontSize: 13 }}>Market Watch</span>
                    <span style={{
                        fontSize: 10, padding: '1px 6px', borderRadius: 3,
                        background: 'var(--theia-badge-background)',
                        color: 'var(--theia-badge-foreground)'
                    }}>DEBUG</span>
                </div>

                <input
                    type="text"
                    placeholder="Filter symbols..."
                    value={filter}
                    onChange={e => setFilter(e.target.value)}
                    style={{
                        flex: 1, maxWidth: 200,
                        padding: '3px 8px', fontSize: 12,
                        background: 'var(--theia-input-background)',
                        color: 'var(--theia-input-foreground)',
                        border: '1px solid var(--theia-input-border)',
                        borderRadius: 4, outline: 'none'
                    }}
                />

                <span style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)', marginLeft: 'auto' }}>
                    {quotes.length} symbol{quotes.length !== 1 ? 's' : ''}
                    {lastUpdate && ` · updated ${lastUpdate.toLocaleTimeString()}`}
                </span>

                <button
                    onClick={fetchQuotes}
                    style={{
                        padding: '3px 10px', fontSize: 11, cursor: 'pointer',
                        background: 'var(--theia-button-background)',
                        color: 'var(--theia-button-foreground)',
                        border: 'none', borderRadius: 4
                    }}
                >↻ Refresh</button>
            </div>

            {error && (
                <div style={{
                    padding: '6px 12px', fontSize: 12,
                    background: 'var(--theia-inputValidation-errorBackground, #5a1d1d)',
                    color: 'var(--theia-errorForeground)',
                    borderBottom: '1px solid var(--theia-inputValidation-errorBorder)',
                    flexShrink: 0
                }}>
                    ⚠ {error}
                </div>
            )}

            {/* Table */}
            <div style={{ flex: 1, overflow: 'auto' }}>
                {filtered.length === 0 ? (
                    <div style={{
                        display: 'flex', flexDirection: 'column', alignItems: 'center',
                        justifyContent: 'center', height: '100%', gap: 8,
                        color: 'var(--theia-descriptionForeground)', fontSize: 13
                    }}>
                        <span style={{ fontSize: 32 }}>📊</span>
                        <span>{filter ? `No symbols matching "${filter}"` : 'No live quotes yet.'}</span>
                        <span style={{ fontSize: 11 }}>
                            {!filter && 'Make sure the Data Feed is connected and symbols are configured.'}
                        </span>
                    </div>
                ) : (
                    <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: 12 }}>
                        <thead>
                            <tr style={{
                                background: 'var(--theia-sideBarSectionHeader-background)',
                                position: 'sticky', top: 0, zIndex: 1
                            }}>
                                <th style={thStyle}>Symbol</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Bid</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Ask</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Spread (pts)</th>
                                <th style={{ ...thStyle, textAlign: 'right' }}>Last Update</th>
                                <th style={{ ...thStyle, textAlign: 'center' }}>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filtered.map(row => (
                                <tr key={row.symbol} style={{
                                    borderBottom: '1px solid var(--theia-panel-border)',
                                    transition: 'background 0.2s'
                                }}>
                                    <td style={{ ...tdStyle, fontWeight: 600, letterSpacing: '0.5px' }}>
                                        {row.symbol}
                                    </td>
                                    <td style={{
                                        ...tdStyle, textAlign: 'right', fontFamily: 'monospace',
                                        fontWeight: 600, fontSize: 13,
                                        color: row.flashBid === 'up' ? '#2ecc71'
                                            : row.flashBid === 'down' ? '#e74c3c'
                                            : 'var(--theia-foreground)',
                                        transition: 'color 0.3s'
                                    }}>
                                        {row.flashBid === 'up' ? '▲ ' : row.flashBid === 'down' ? '▼ ' : ''}
                                        {formatPrice(row.bid)}
                                    </td>
                                    <td style={{
                                        ...tdStyle, textAlign: 'right', fontFamily: 'monospace',
                                        fontWeight: 600, fontSize: 13,
                                        color: row.flashAsk === 'up' ? '#2ecc71'
                                            : row.flashAsk === 'down' ? '#e74c3c'
                                            : 'var(--theia-foreground)',
                                        transition: 'color 0.3s'
                                    }}>
                                        {row.flashAsk === 'up' ? '▲ ' : row.flashAsk === 'down' ? '▼ ' : ''}
                                        {formatPrice(row.ask)}
                                    </td>
                                    <td style={{ ...tdStyle, textAlign: 'right', color: 'var(--theia-descriptionForeground)' }}>
                                        {row.spread.toFixed(1)}
                                    </td>
                                    <td style={{ ...tdStyle, textAlign: 'right', color: ageColor(row.age), fontFamily: 'monospace' }}>
                                        {formatAge(row.age)}
                                    </td>
                                    <td style={{ ...tdStyle, textAlign: 'center' }}>
                                        <span style={{
                                            display: 'inline-block', width: 7, height: 7,
                                            borderRadius: '50%',
                                            background: row.age < 5 ? '#2ecc71' : row.age < 30 ? '#f1c40f' : '#e74c3c',
                                            boxShadow: row.age < 5 ? '0 0 5px #2ecc7188' : 'none'
                                        }} />
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>

            <style>{`
                @keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.4} }
            `}</style>
        </div>
    );
}

const thStyle: React.CSSProperties = {
    padding: '6px 10px',
    textAlign: 'left',
    fontWeight: 600,
    fontSize: 11,
    textTransform: 'uppercase',
    letterSpacing: '0.5px',
    color: 'var(--theia-descriptionForeground)',
    borderBottom: '1px solid var(--theia-panel-border)',
    whiteSpace: 'nowrap'
};

const tdStyle: React.CSSProperties = {
    padding: '5px 10px',
    whiteSpace: 'nowrap'
};

```

---

<a id='browser-modules-network-cluster-networkclusterpage-tsx'></a>
### 63. `browser/modules/network-cluster/NetworkClusterPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';

/** Network Cluster — Main overview: lists all servers with Type/Address/CPU/Connections */
export function NetworkClusterOverview(): React.ReactElement {
    const [statuses, setStatuses] = React.useState<Record<string, boolean>>({
        trade: false,
        history: false,
        access: false,
        backup: false
    });

    const checkServerStatus = async () => {
        const nextStatuses = { ...statuses };
        
        // 1. Trade Server (port 8000)
        try {
            const resp = await fetch('http://localhost:8000/accounts/10001', { method: 'HEAD' });
            nextStatuses.trade = true;
        } catch {
            nextStatuses.trade = false;
        }

        // 2. History Server (port 8002)
        try {
            await fetch('http://localhost:8002/', { method: 'HEAD' });
            nextStatuses.history = true;
        } catch {
            nextStatuses.history = false;
        }

        // 3. Access Server (port 8001)
        try {
            await fetch('http://localhost:8001/', { method: 'HEAD' });
            nextStatuses.access = true;
        } catch {
            nextStatuses.access = false;
        }

        // 4. Backup Server (port 8004)
        try {
            await fetch('http://localhost:8004/', { method: 'HEAD' });
            nextStatuses.backup = true;
        } catch {
            nextStatuses.backup = false;
        }

        setStatuses(nextStatuses);
    };

    React.useEffect(() => {
        checkServerStatus();
        const interval = setInterval(checkServerStatus, 5000);
        return () => clearInterval(interval);
    }, []);

    const servers = [
        { id: '1', type: 'Main Trade Server', name: 'MetaQuotes-Demo', address: '127.0.0.1:8000', pubAddr: '127.0.0.1', conns: statuses.trade ? 142 : 0, basePri: 1, curPri: 1, cpu: statuses.trade ? 8 : 0, online: statuses.trade },
        { id: '2', type: 'History Server',     name: 'History-01',     address: '127.0.0.1:8002',      pubAddr: '127.0.0.1',      conns: statuses.history ? 1 : 0,   basePri: 1, curPri: 1, cpu: statuses.history ? 4 : 0,  online: statuses.history },
        { id: '3', type: 'Access Server',      name: 'Access-01',      address: '127.0.0.1:8001',      pubAddr: '127.0.0.1',      conns: statuses.access ? 3 : 0,   basePri: 1, curPri: 1, cpu: statuses.access ? 2 : 0,  online: statuses.access },
        { id: '4', type: 'Backup Server',      name: 'Backup-01',      address: '127.0.0.1:8004',      pubAddr: '127.0.0.1',      conns: 0,   basePri: 2, curPri: 2, cpu: 0,  online: statuses.backup },
    ];

    const [sel, setSel] = React.useState<string | null>(null);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn" onClick={checkServerStatus} title="Reload statuses"><i className="codicon codicon-refresh" /> Refresh</button>
            </div>
            <div className="adm-hint"><i className="codicon codicon-info" />Red icon means the server is offline or unreachable on its configured local port.</div>
            <div className="adm-table-wrap">
                <table className="adm-table">
                    <thead><tr><th></th><th>Type</th><th>Server Name</th><th>Address</th><th>Public Addresses</th><th>ID</th><th>Connections</th><th>Base Priority</th><th>Current Priority</th><th>CPU %</th></tr></thead>
                    <tbody>
                        {servers.map(s => (
                            <tr key={s.id} className={sel === s.id ? 'selected' : ''} onClick={() => setSel(s.id)}>
                                <td><span className={`adm-status-dot ${s.online ? 'online' : 'offline'}`} /></td>
                                <td><span className="adm-tag">{s.type}</span></td>
                                <td><strong>{s.name}</strong></td>
                                <td><code className="adm-code">{s.address}</code></td>
                                <td><code className="adm-code">{s.pubAddr}</code></td>
                                <td>{s.id}</td>
                                <td className="adm-num">{s.conns}</td>
                                <td className="adm-num">{s.basePri}</td>
                                <td className="adm-num">{s.curPri}</td>
                                <td>
                                    <div className="adm-cpu-bar">
                                        <div className="adm-cpu-fill" style={{ width: `${s.cpu}%`, background: s.cpu > 80 ? 'var(--theia-errorForeground)' : s.cpu > 50 ? '#f0ad4e' : '#27ae60' }} />
                                        <span>{s.cpu}%</span>
                                    </div>
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="adm-statusbar">
                <span>Servers: {servers.length}</span>
                <span className="adm-sep">|</span>
                <span style={{ color: '#27ae60' }}>Online: {servers.filter(s => s.online).length}</span>
                <span className="adm-sep">|</span>
                <span style={{ color: 'var(--theia-errorForeground)' }}>Offline: {servers.filter(s => !s.online).length}</span>
            </div>
        </div>
    );
}

/** Network Cluster — Servers: configure individual server settings (Common / Network / Service tabs) */
export function NetworkServersPage(): React.ReactElement {
    const [tab, setTab] = React.useState<'common' | 'network' | 'service'>('common');
    const serverTypes = ['Main Trade Server', 'Trade Server', 'History Server', 'Access Server', 'Backup Server'];
    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn adm-btn-primary" disabled><i className="codicon codicon-add" /> Add Server</button>
            </div>
            <div className="adm-tabs">
                {(['common', 'network', 'service'] as const).map(t => (
                    <button key={t} className={`adm-tab ${tab === t ? 'active' : ''}`} onClick={() => setTab(t)}>{t.charAt(0).toUpperCase() + t.slice(1)}</button>
                ))}
            </div>
            {tab === 'common' && (
                <div className="adm-form-body">
                    <div className="adm-form-section">General</div>
                    <div className="adm-form-row"><label>Type</label><select className="adm-select" disabled>{serverTypes.map(t => <option key={t}>{t}</option>)}</select></div>
                    <div className="adm-form-row"><label>Name</label><input className="adm-input" readOnly defaultValue="MetaQuotes-Demo" /></div>
                    <div className="adm-form-row"><label>ID</label><input className="adm-input" readOnly defaultValue="1" type="number" /></div>
                    <div className="adm-form-row"><label>Password</label><input className="adm-input" readOnly type="password" value="******" /></div>
                    <div className="adm-form-section">Geo Location</div>
                    <div className="adm-form-row"><label>Latitude</label><input className="adm-input" readOnly defaultValue="0.0000" /></div>
                    <div className="adm-form-row"><label>Longitude</label><input className="adm-input" readOnly defaultValue="0.0000" /></div>
                </div>
            )}
            {tab === 'network' && (
                <div className="adm-form-body">
                    <div className="adm-form-section">IPv4 Settings</div>
                    <div className="adm-form-row"><label>Listen Address (IPv4)</label><input className="adm-input" readOnly defaultValue="0.0.0.0:8000" /></div>
                    <div className="adm-form-row"><label>Outgoing Address (IPv4)</label><input className="adm-input" readOnly defaultValue="127.0.0.1:0" /></div>
                    <div className="adm-form-section">Public Addresses</div>
                    <div className="adm-form-row"><label>Public Addresses</label><textarea className="adm-input" readOnly style={{ height: 40 }} defaultValue="127.0.0.1" /></div>
                </div>
            )}
            {tab === 'service' && (
                <div className="adm-form-body">
                    <div className="adm-form-section">Service Management</div>
                    <div className="adm-form-row"><label>Service Name</label><input className="adm-input" readOnly defaultValue="MT5TradeServer" /></div>
                    <div className="adm-form-row"><label>Startup Type</label><select className="adm-select" disabled><option>Automatic</option></select></div>
                </div>
            )}
        </div>
    );
}

/** Network Cluster — Data Centers */
export function NetworkDataCentersPage(): React.ReactElement {
    const dcs = [
        { id: '1', name: 'DC-Main', region: 'US-East',   ip: '127.0.0.1', servers: 3, latency: 1  },
    ];
    return (
        <div className="adm-page">
            <div className="adm-table-wrap">
                <table className="adm-table">
                    <thead><tr><th>Name</th><th>Region</th><th>IP Address</th><th>Servers</th><th>Latency (ms)</th></tr></thead>
                    <tbody>
                        {dcs.map(dc => (
                            <tr key={dc.id}>
                                <td><strong>{dc.name}</strong></td>
                                <td>{dc.region}</td>
                                <td><code className="adm-code">{dc.ip}</code></td>
                                <td>{dc.servers}</td>
                                <td className="adm-num" style={{ color: '#27ae60' }}>{dc.latency} ms</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            <div className="adm-statusbar"><span>Data Centers: {dcs.length}</span></div>
        </div>
    );
}

/** Network Cluster — Backup Server configuration */
export function NetworkBackupPage(): React.ReactElement {
    return (
        <div className="adm-page">
            <div className="adm-form-body" style={{ maxWidth: 520 }}>
                <div className="adm-form-section">Backup Server Settings</div>
                <div className="adm-form-row"><label>Backup Server</label><select className="adm-select" disabled><option>Backup-01 (127.0.0.1:8004)</option></select></div>
                <div className="adm-form-row"><label>Backed Up Server</label><select className="adm-select" disabled><option>Main Trade Server</option></select></div>
                <div className="adm-form-row"><label>Status</label><span style={{ color: 'var(--theia-errorForeground)', padding: '3px 0' }}>● Offline</span></div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-orders-orderspage-tsx'></a>
### 63. `browser/modules/orders/OrdersPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

interface Order {
    ticket: number;
    login: number;
    symbol: string;
    volume: number;
    volume_current: number;
    price_order: number;
    price_sl: number;
    price_tp: number;
    type: number; // 0=BUY, 1=SELL, 2=BUY LIMIT, 3=SELL LIMIT, 4=BUY STOP, 5=SELL STOP
    state: number; // 0=STARTED, 1=PARTIAL, 4=FILLED, 5=REJECTED/CANCELED, 6=PENDING_DEALER, 7=PENDING_GATEWAY
    reason: number;
    time_setup: string;
    time_done?: string;
}

const TYPE_MAP: Record<number, string> = {
    0: 'BUY',
    1: 'SELL',
    2: 'BUY LIMIT',
    3: 'SELL LIMIT',
    4: 'BUY STOP',
    5: 'SELL STOP'
};

const STATE_MAP: Record<number, string> = {
    0: 'PLACED',
    1: 'PARTIAL',
    4: 'FILLED',
    5: 'CANCELED',
    6: 'DEALER',
    7: 'GATEWAY'
};

const TYPE_COLOR: Record<string, string> = {
    'BUY':        '#27ae60', 'BUY LIMIT': '#2ecc71', 'BUY STOP': '#16a085',
    'SELL':       '#e74c3c', 'SELL LIMIT':'#c0392b', 'SELL STOP':'#922b21',
};
const STATE_COLOR: Record<string, string> = {
    PLACED: '#3498db', PARTIAL: '#f39c12', CANCELED: '#95a5a6', FILLED: '#27ae60', DEALER: '#9b59b6', GATEWAY: '#e67e22'
};

interface Props { view: 'active' | 'history' | 'new'; }

export function OrdersPage({ view }: Props): React.ReactElement {
    const [orders, setOrders] = React.useState<Order[]>([]);
    const [sel, setSel] = React.useState<number | null>(null);
    const [filter, setFilter] = React.useState('');
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Initial configuration lists
    const [accounts, setAccounts] = React.useState<any[]>([]);
    const [symbols, setSymbols] = React.useState<any[]>([]);
    const [groups, setGroups] = React.useState<any[]>([]);
    const [ticks, setTicks] = React.useState<Record<string, { bid: number; ask: number; age: number }>>({});

    // Hierarchical tree state
    const [treeOpen, setTreeOpen] = React.useState(false);
    const [searchQuery, setSearchQuery] = React.useState('');
    const [expandedFolders, setExpandedFolders] = React.useState<Record<string, boolean>>({
        'forex': true, 'Metals': true, 'crypto': true, 'Custom': true
    });

    // New order form state
    const [newOrder, setNewOrder] = React.useState({
        login: '',
        symbol: 'forex\\EURUSD',
        type: '0', // OP_BUY
        volume: '0.10',
        price_request: '',
        price_sl: '0',
        price_tp: '0',
        type_filling: 'FOK',
        comment: ''
    });
    const [formMsg, setFormMsg] = React.useState<{ status: 'SUCCESS' | 'ERROR'; text: string } | null>(null);

    // Compute if the selected symbol is allowed under the current account's group settings
    const isSymbolAllowed = React.useMemo(() => {
        if (!newOrder.symbol) return true;
        const selectedAcc = accounts.find(a => String(a.login) === String(newOrder.login));
        if (!selectedAcc) return true;

        const groupName = selectedAcc.group_name;
        const group = groups.find(g => g.name === groupName);
        if (!group) return true;

        let symbolRules: any[] = [];
        if (group.settings_json) {
            try {
                const settings = typeof group.settings_json === 'string' ? JSON.parse(group.settings_json) : group.settings_json;
                symbolRules = settings.symbol_rules || [];
            } catch {}
        }

        if (symbolRules.length === 0) return true;

        let matchingRules = symbolRules.filter(rule => {
            try {
                const pattern = rule.symbol;
                const regexStr = '^' + pattern
                    .replace(/[\-+^${}()|[\]\.]/g, '\\$&')
                    .replace(/\\/g, '\\\\')
                    .replace(/\*/g, '.*')
                    .replace(/\?/g, '.') + '$';
                const regex = new RegExp(regexStr, 'i');
                return regex.test(newOrder.symbol);
            } catch {
                return false;
            }
        });

        if (matchingRules.length === 0) return false;
        matchingRules.sort((a, b) => b.symbol.length - a.symbol.length);
        return matchingRules[0].trade_allowed;
    }, [newOrder.symbol, newOrder.login, accounts, groups]);

    // Parse symbols list into directory structure
    const tree = React.useMemo(() => {
        const root: any = { files: [], dirs: {} };
        symbols.forEach(s => {
            const parts = s.symbol.split('\\');
            let curr = root;
            for (let i = 0; i < parts.length - 1; i++) {
                const dirName = parts[i];
                if (!curr.dirs[dirName]) {
                    curr.dirs[dirName] = { name: dirName, files: [], dirs: {} };
                }
                curr = curr.dirs[dirName];
            }
            curr.files.push(s.symbol);
        });
        return root;
    }, [symbols]);

    // Live price variables for the selected symbol
    const currentTick = ticks[newOrder.symbol] || ticks[newOrder.symbol.split('\\').pop() || ''] || null;
    const bidPrice = currentTick ? currentTick.bid : 1.08000;
    const askPrice = currentTick ? currentTick.ask : 1.08010;

    const loadOrders = async () => {
        setLoading(true);
        setError(null);
        try {
            if (view === 'active') {
                const data = await API.getOrders();
                setOrders(data);
            } else if (view === 'history') {
                const data = await API.getOrderHistory();
                setOrders(data);
            }
        } catch (err: any) {
            setError(err.message || 'Failed to load orders.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        if (view !== 'new') {
            loadOrders();
        } else {
            // Load setup metadata
            const loadMetadata = async () => {
                try {
                    const [accs, syms, grps] = await Promise.all([
                        API.getAccounts(),
                        API.getSymbols(),
                        API.getGroups()
                    ]);
                    setAccounts(accs);
                    setSymbols(syms);
                    setGroups(grps);
                    if (accs.length > 0) {
                        setNewOrder(prev => ({ ...prev, login: String(accs[0].login) }));
                    }
                    if (syms.length > 0) {
                        // Select first symbol path that is not dummy
                        const valid = syms.find(s => !s.symbol.includes('.dummy'));
                        if (valid) {
                            setNewOrder(prev => ({ ...prev, symbol: valid.symbol }));
                        }
                    }
                } catch (err: any) {
                    setError(err.message || 'Failed to load accounts, symbols, and groups list.');
                }
            };
            loadMetadata();

            // Setup tick polling interval
            const tickPoll = setInterval(async () => {
                try {
                    const data = await API.getTicks();
                    setTicks(data);
                } catch {
                    // Ignore transient network errors
                }
            }, 1000);
            return () => clearInterval(tickPoll);
        }
    }, [view]);

    const handleExecuteOrder = async (overrideType?: number, overridePrice?: number) => {
        setFormMsg(null);
        try {
            const login = parseInt(newOrder.login);
            if (!login) throw new Error('Please select a valid account login.');

            const oType = overrideType !== undefined ? overrideType : parseInt(newOrder.type);
            
            let price_req = overridePrice !== undefined ? overridePrice : parseFloat(newOrder.price_request);
            if ([0, 1].includes(oType)) {
                // If it is market buy or sell, default to streaming quotes if empty
                if (!price_req) {
                    price_req = oType === 0 ? askPrice : bidPrice;
                }
            } else {
                if (!price_req) throw new Error('Execution trigger price is required for pending orders.');
            }

            const payload = {
                login,
                symbol: newOrder.symbol,
                volume: parseFloat(newOrder.volume) || 0.1,
                price_request: price_req,
                type: oType,
                price_sl: parseFloat(newOrder.price_sl) || 0,
                price_tp: parseFloat(newOrder.price_tp) || 0,
                type_filling: newOrder.type_filling
            };

            const resp = await API.placeOrder(payload);
            setFormMsg({ 
                status: 'SUCCESS', 
                text: `Order filled successfully! Ticket #${resp.ticket}. Match status: ${resp.status}. Detail: ${resp.message}` 
            });
        } catch (err: any) {
            setFormMsg({ status: 'ERROR', text: err.message || 'Order execution failed.' });
        }
    };

    const handlePlaceOrder = async (e: React.FormEvent) => {
        e.preventDefault();
        await handleExecuteOrder();
    };

    const handleCancelOrder = async () => {
        if (!sel) return;
        setError(null);
        try {
            await API.cancelOrder(sel);
            setSel(null);
            await loadOrders();
        } catch (err: any) {
            setError(err.message || 'Failed to cancel order.');
        }
    };

    const renderNode = (node: any, path: string = '', depth: number = 0) => {
        const elements: any[] = [];
        
        // Render directories
        Object.keys(node.dirs).sort().forEach(dirName => {
            const dir = node.dirs[dirName];
            const fullDirPath = path ? `${path}\\${dirName}` : dirName;
            const isExpanded = !!expandedFolders[fullDirPath];
            elements.push(
                <div key={fullDirPath} style={{ paddingLeft: depth * 10 }}>
                    <div 
                        style={{ 
                            display: 'flex', 
                            alignItems: 'center', 
                            gap: 6, 
                            height: 24, 
                            cursor: 'pointer', 
                            opacity: 0.9,
                            fontSize: '11.5px',
                            fontWeight: 600,
                            color: 'var(--theia-descriptionForeground)'
                        }}
                        onClick={(e) => {
                            e.stopPropagation();
                            setExpandedFolders(prev => ({ ...prev, [fullDirPath]: !isExpanded }));
                        }}
                    >
                        <i className={`codicon ${isExpanded ? 'codicon-chevron-down' : 'codicon-chevron-right'}`} style={{ fontSize: 10 }} />
                        <i className="codicon codicon-folder" style={{ color: '#f39c12', fontSize: 12 }} />
                        <span>{dirName}</span>
                    </div>
                    {isExpanded && renderNode(dir, fullDirPath, depth + 1)}
                </div>
            );
        });
        
        // Render leaf files
        node.files.sort().forEach((symPath: string) => {
            const baseName = symPath.split('\\').pop() || symPath;
            if (baseName.includes('.dummy')) return; // hide dummy nodes
            
            elements.push(
                <div 
                    key={symPath} 
                    style={{ 
                        paddingLeft: (depth * 10) + 16, 
                        display: 'flex', 
                        alignItems: 'center', 
                        gap: 6, 
                        height: 24, 
                        cursor: 'pointer',
                        background: newOrder.symbol === symPath ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                        color: newOrder.symbol === symPath ? 'var(--theia-list-activeSelectionForeground)' : 'inherit',
                        borderRadius: 3,
                        fontSize: '11px'
                    }}
                    onClick={(e) => {
                        e.stopPropagation();
                        setNewOrder(prev => ({ ...prev, symbol: symPath }));
                        setTreeOpen(false);
                    }}
                >
                    <i className="codicon codicon-symbol-variable" style={{ fontSize: 11, opacity: 0.8 }} />
                    <span>{baseName}</span>
                </div>
            );
        });
        
        return elements;
    };

    if (view === 'new') {
        const isMarket = ['0', '1'].includes(newOrder.type);
        const filteredSymbols = symbols.filter(s => 
            s.symbol.toLowerCase().includes(searchQuery.toLowerCase()) && !s.symbol.includes('.dummy')
        );

        return (
            <div className="adm-page">
                <form onSubmit={handlePlaceOrder} style={{ display: 'flex', flexDirection: 'column', height: '100%' }}>
                    <div className="adm-toolbar">
                        {!isMarket && (
                            <button type="submit" className="adm-btn adm-btn-primary">
                                <i className="codicon codicon-check" /> Place Pending Order
                            </button>
                        )}
                        <button 
                            type="button" 
                            className="adm-btn" 
                            onClick={() => {
                                setFormMsg(null);
                                setNewOrder({
                                    login: accounts.length > 0 ? String(accounts[0].login) : '',
                                    symbol: symbols.length > 0 ? symbols[0].symbol : 'forex\\EURUSD',
                                    type: '0',
                                    volume: '0.10',
                                    price_request: '',
                                    price_sl: '0',
                                    price_tp: '0',
                                    type_filling: 'FOK',
                                    comment: ''
                                });
                            }}
                        >
                            <i className="codicon codicon-discard" /> Reset fields
                        </button>
                    </div>
                    {formMsg && (
                        <div className="adm-hint" style={{
                            background: formMsg.status === 'SUCCESS' ? 'var(--theia-inputValidation-infoBackground)' : 'var(--theia-inputValidation-errorBackground)',
                            color: formMsg.status === 'SUCCESS' ? 'var(--theia-successForeground)' : 'var(--theia-errorForeground)'
                        }}>
                            <i className={formMsg.status === 'SUCCESS' ? 'codicon codicon-info' : 'codicon codicon-error'} /> {formMsg.text}
                        </div>
                    )}
                    <div className="adm-form-body" style={{ maxWidth: 520 }}>
                        <div className="adm-form-section">1. Client Account</div>
                        <div className="adm-form-row">
                            <label>Login ID</label>
                            <select 
                                className="adm-select" 
                                style={{ width: 320 }}
                                value={newOrder.login} 
                                onChange={e => setNewOrder({ ...newOrder, login: e.target.value })}
                            >
                                {accounts.length === 0 ? (
                                    <option value="">No accounts found</option>
                                ) : (
                                    accounts.map(acc => (
                                        <option key={acc.login} value={acc.login}>
                                            {acc.login} ({acc.group_name}) — Balance: ${acc.balance.toLocaleString('en-US', { minimumFractionDigits: 2 })}
                                        </option>
                                    ))
                                )}
                            </select>
                        </div>

                        <div className="adm-form-section">2. Instrument & Volume</div>
                        <div className="adm-form-row" style={{ zIndex: 100 }}>
                            <label>Symbol Path</label>
                            <div style={{ position: 'relative', width: 320 }}>
                                <div 
                                    className="adm-select" 
                                    style={{ 
                                        display: 'flex', 
                                        justifyContent: 'space-between', 
                                        alignItems: 'center', 
                                        width: '100%', 
                                        boxSizing: 'border-box',
                                        background: 'var(--theia-input-background)',
                                        border: '1px solid var(--theia-input-border)',
                                        cursor: 'pointer'
                                    }}
                                    onClick={() => setTreeOpen(!treeOpen)}
                                >
                                    <span style={{ fontFamily: 'monospace' }}>{newOrder.symbol || 'Choose platform path...'}</span>
                                    <i className={`codicon ${treeOpen ? 'codicon-chevron-up' : 'codicon-chevron-down'}`} />
                                </div>
                                {!isSymbolAllowed && (
                                    <div style={{
                                        color: 'var(--theia-errorForeground)',
                                        fontSize: '11px',
                                        marginTop: 4,
                                        display: 'flex',
                                        alignItems: 'center',
                                        gap: 4
                                    }}>
                                        <i className="codicon codicon-warning" style={{ fontSize: 12 }} />
                                        <span>Warning: Trading is not allowed for this symbol under your group settings</span>
                                    </div>
                                )}
                                {treeOpen && (
                                    <div style={{
                                        position: 'absolute',
                                        top: '100%',
                                        left: 0,
                                        width: '100%',
                                        maxHeight: 220,
                                        overflowY: 'auto',
                                        background: 'var(--theia-editor-background)',
                                        border: '1px solid var(--theia-widget-border)',
                                        borderRadius: '0 0 4px 4px',
                                        zIndex: 1000,
                                        boxShadow: '0 4px 16px rgba(0,0,0,0.5)',
                                        padding: 8,
                                        boxSizing: 'border-box'
                                    }}>
                                        <input 
                                            className="adm-input" 
                                            placeholder="Filter symbols..." 
                                            style={{ width: '100%', marginBottom: 8, boxSizing: 'border-box' }}
                                            value={searchQuery}
                                            onChange={e => setSearchQuery(e.target.value)}
                                            onClick={e => e.stopPropagation()}
                                        />
                                        {searchQuery ? (
                                            filteredSymbols.length === 0 ? (
                                                <div style={{ opacity: 0.5, padding: 4 }}>No symbols match</div>
                                            ) : (
                                                filteredSymbols.map(s => (
                                                    <div 
                                                        key={s.symbol}
                                                        style={{ 
                                                            display: 'flex', 
                                                            alignItems: 'center', 
                                                            gap: 6, 
                                                            height: 22, 
                                                            cursor: 'pointer',
                                                            padding: '2px 6px',
                                                            borderRadius: 3,
                                                            background: newOrder.symbol === s.symbol ? 'var(--theia-list-activeSelectionBackground)' : 'transparent',
                                                            color: newOrder.symbol === s.symbol ? 'var(--theia-list-activeSelectionForeground)' : 'inherit',
                                                            fontSize: '11px'
                                                        }}
                                                        onClick={(e) => {
                                                            e.stopPropagation();
                                                            setNewOrder(prev => ({ ...prev, symbol: s.symbol }));
                                                            setTreeOpen(false);
                                                        }}
                                                    >
                                                        <i className="codicon codicon-symbol-variable" />
                                                        <span>{s.symbol}</span>
                                                    </div>
                                                ))
                                            )
                                        ) : (
                                            renderNode(tree)
                                        )}
                                    </div>
                                )}
                            </div>
                        </div>

                        <div className="adm-form-row">
                            <label>Volume (Lots)</label>
                            <div style={{ display: 'flex', gap: 6, alignItems: 'center' }}>
                                <input 
                                    className="adm-input" 
                                    type="number" 
                                    step="0.01" 
                                    min="0.01" 
                                    value={newOrder.volume} 
                                    onChange={e => setNewOrder({ ...newOrder, volume: e.target.value })} 
                                />
                                {['0.01', '0.10', '1.00', '10.00'].map(vol => (
                                    <button 
                                        type="button" 
                                        key={vol} 
                                        className="adm-btn" 
                                        style={{ padding: '3px 6px', fontSize: 10 }}
                                        onClick={() => setNewOrder({ ...newOrder, volume: vol })}
                                    >
                                        {vol} Lot
                                    </button>
                                ))}
                            </div>
                        </div>

                        <div className="adm-form-section">3. Execution & Price</div>
                        <div className="adm-form-row">
                            <label>Order Type</label>
                            <select 
                                className="adm-select" 
                                style={{ width: 320 }}
                                value={newOrder.type} 
                                onChange={e => setNewOrder({ ...newOrder, type: e.target.value })}
                            >
                                <option value="0">Buy (Market)</option>
                                <option value="1">Sell (Market)</option>
                                <option value="2">Buy Limit (Pending)</option>
                                <option value="3">Sell Limit (Pending)</option>
                                <option value="4">Buy Stop (Pending)</option>
                                <option value="5">Sell Stop (Pending)</option>
                            </select>
                        </div>

                        {/* Interactive BUY/SELL Execution Panel for Market Orders */}
                        {isMarket && (
                            <div style={{ margin: '14px 0', width: 320 }}>
                                <div style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)', marginBottom: 6, fontWeight: 600 }}>
                                    Live streaming quotes (Click bid/ask to execute instantly)
                                </div>
                                <div style={{ display: 'flex', gap: 12 }}>
                                    <button 
                                        type="button"
                                        className="adm-btn"
                                        style={{ 
                                            flex: 1, 
                                            height: 52, 
                                            display: 'flex', 
                                            flexDirection: 'column', 
                                            alignItems: 'center', 
                                            justifyContent: 'center',
                                            borderColor: '#e74c3c',
                                            color: '#fff',
                                            background: '#e74c3c',
                                            borderRadius: 4
                                        }}
                                        onClick={() => handleExecuteOrder(1, bidPrice)}
                                    >
                                        <span style={{ fontSize: 10, fontWeight: 700, opacity: 0.9 }}>SELL (Market)</span>
                                        <span style={{ fontSize: 16, fontWeight: 700, fontFamily: 'monospace', letterSpacing: 0.5 }}>{bidPrice.toFixed(5)}</span>
                                    </button>
                                    <button 
                                        type="button"
                                        className="adm-btn adm-btn-primary"
                                        style={{ 
                                            flex: 1, 
                                            height: 52, 
                                            display: 'flex', 
                                            flexDirection: 'column', 
                                            alignItems: 'center', 
                                            justifyContent: 'center',
                                            background: '#27ae60',
                                            borderColor: 'transparent',
                                            color: '#fff',
                                            borderRadius: 4
                                        }}
                                        onClick={() => handleExecuteOrder(0, askPrice)}
                                    >
                                        <span style={{ fontSize: 10, fontWeight: 700, opacity: 0.9 }}>BUY (Market)</span>
                                        <span style={{ fontSize: 16, fontWeight: 700, fontFamily: 'monospace', letterSpacing: 0.5 }}>{askPrice.toFixed(5)}</span>
                                    </button>
                                </div>
                                {currentTick && (
                                    <div style={{ fontSize: 10, opacity: 0.6, marginTop: 4, textAlign: 'center' }}>
                                        Quote latency: {currentTick.age.toFixed(1)}s old
                                    </div>
                                )}
                            </div>
                        )}

                        {!isMarket && (
                            <div className="adm-form-row">
                                <label>Pending Activation Price</label>
                                <input 
                                    className="adm-input" 
                                    type="number" 
                                    step="0.00001" 
                                    placeholder="Enter target trigger price" 
                                    value={newOrder.price_request} 
                                    onChange={e => setNewOrder({ ...newOrder, price_request: e.target.value })} 
                                />
                            </div>
                        )}

                        <div className="adm-form-row">
                            <label>Stop Loss (SL)</label>
                            <input 
                                className="adm-input" 
                                type="number" 
                                step="0.00001" 
                                placeholder="0 = No SL limits" 
                                value={newOrder.price_sl} 
                                onChange={e => setNewOrder({ ...newOrder, price_sl: e.target.value })} 
                            />
                        </div>
                        <div className="adm-form-row">
                            <label>Take Profit (TP)</label>
                            <input 
                                className="adm-input" 
                                type="number" 
                                step="0.00001" 
                                placeholder="0 = No TP limits" 
                                value={newOrder.price_tp} 
                                onChange={e => setNewOrder({ ...newOrder, price_tp: e.target.value })} 
                            />
                        </div>

                        <div className="adm-form-section">4. Filling Policy & Meta</div>
                        <div className="adm-form-row">
                            <label>Filling Policy (Mode)</label>
                            <select 
                                className="adm-select" 
                                style={{ width: 320 }}
                                value={newOrder.type_filling} 
                                onChange={e => setNewOrder({ ...newOrder, type_filling: e.target.value })}
                            >
                                <option value="FOK">Fill or Kill (FOK)</option>
                                <option value="IOC">Immediate or Cancel (IOC)</option>
                                <option value="RETURN">Return (Partial execution allowed)</option>
                            </select>
                            <span className="adm-hint-text" style={{ maxWidth: 320 }}>
                                FOK executes full size or cancels. IOC executes what matches, cancels remainder. Return allows partial matches.
                            </span>
                        </div>
                        <div className="adm-form-row">
                            <label>Order Comment</label>
                            <input 
                                className="adm-input" 
                                placeholder="Enter audit/test remarks" 
                                style={{ width: 320 }} 
                                value={newOrder.comment} 
                                onChange={e => setNewOrder({ ...newOrder, comment: e.target.value })} 
                            />
                        </div>
                    </div>
                </form>
            </div>
        );
    }

    const filtered = orders.filter(o =>
        String(o.login).includes(filter) ||
        o.symbol.toLowerCase().includes(filter.toLowerCase()) ||
        String(o.ticket).includes(filter)
    );

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                {view === 'active' && <>
                    <button className="adm-btn adm-btn-danger" disabled={!sel} onClick={handleCancelOrder}><i className="codicon codicon-close" /> Cancel Order</button>
                    <div className="adm-toolbar-sep" />
                </>}
                <button className="adm-btn" onClick={loadOrders} title="Reload data">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div className="adm-toolbar-sep" />
                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input className="adm-search" placeholder="Filter by login, symbol, ticket..." value={filter} onChange={e => setFilter(e.target.value)} />
                </div>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading orders...</div>
                ) : filtered.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No orders found.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th>Ticket</th><th>Login</th><th>Symbol</th><th>Type</th><th>Volume</th><th>Current Volume</th>
                                <th>Order Price</th><th>S/L</th><th>T/P</th><th>State</th><th>Reason</th><th>Time Placed</th>
                                {view === 'history' && <th>Time Settled</th>}
                            </tr>
                        </thead>
                        <tbody>
                            {filtered.map(o => {
                                const typeStr = TYPE_MAP[o.type] || 'UNKNOWN';
                                const stateStr = STATE_MAP[o.state] || 'UNKNOWN';
                                const reasonStr = o.reason === 0 ? 'CLIENT' : o.reason === 4 ? 'S/L' : o.reason === 5 ? 'T/P' : 'S/O';
                                
                                return (
                                    <tr key={o.ticket} className={sel === o.ticket ? 'selected' : ''} onClick={() => setSel(o.ticket)}>
                                        <td><strong>{o.ticket}</strong></td>
                                        <td>{o.login}</td>
                                        <td><strong>{o.symbol}</strong></td>
                                        <td>
                                            <span className="adm-side-badge" style={{
                                                background: (TYPE_COLOR[typeStr] || '#888') + '22',
                                                color: TYPE_COLOR[typeStr] || '#888',
                                                border: `1px solid ${(TYPE_COLOR[typeStr] || '#888')}55`
                                            }}>{typeStr}</span>
                                        </td>
                                        <td>{(o.volume || 0).toFixed(2)}</td>
                                        <td>{(o.volume_current || 0).toFixed(2)}</td>
                                        <td className="adm-num">{(o.price_order || 0).toFixed(5)}</td>
                                        <td className="adm-num">{o.price_sl || '—'}</td>
                                        <td className="adm-num">{o.price_tp || '—'}</td>
                                        <td>
                                            <span className="adm-tag" style={{
                                                color: STATE_COLOR[stateStr] || '#aaa',
                                                border: `1px solid ${(STATE_COLOR[stateStr] || '#aaa')}55`
                                            }}>{stateStr}</span>
                                        </td>
                                        <td>{reasonStr}</td>
                                        <td>{o.time_setup || '—'}</td>
                                        {view === 'history' && <td>{o.time_done || '—'}</td>}
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                )}
            </div>

            <div className="adm-statusbar">
                <span>{view === 'active' ? 'Active' : 'Settled'} Orders: {filtered.length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-positions-exposurepage-tsx'></a>
### 63. `browser/modules/positions/ExposurePage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

export function ExposurePage(): React.ReactElement {
    const [exposureData, setExposureData] = React.useState<any[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);
    const [displayCurrency, setDisplayCurrency] = React.useState('USD');

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getRiskExposure();
            setExposureData(data);
        } catch (err: any) {
            setError(err.message || 'Failed to load Exposure data.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    // Calculated Exposure mapped to custom Display Currency
    const mappedExposure = React.useMemo(() => {
        // Mock conversion rates relative to display currency if needed
        const mockRates: Record<string, number> = {
            'USD': 1.0,
            'EUR': 1.09,
            'GBP': 1.27,
            'JPY': 0.0067,
            'NZD': 0.61,
            'AUD': 0.66,
            'NOK': 0.095,
            'BTC': 62000.0,
            'XAU': 2350.0,
            'XAG': 29.5
        };

        // Standardize everything to displayCurrency
        const currentDisplayRate = mockRates[displayCurrency] || 1.0;

        return exposureData.map(d => {
            const assetRate = mockRates[d.asset] || 1.0;
            // Cross-convert rate from asset to target display currency
            const rate = assetRate / currentDisplayRate;
            const netTotalConverted = d.netTotal * rate;
            const positiveConverted = netTotalConverted > 0 ? netTotalConverted : 0;

            return {
                ...d,
                rate,
                netTotalConverted,
                positiveConverted
            };
        });
    }, [exposureData, displayCurrency]);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn" onClick={loadData}>
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div className="adm-toolbar-sep" />
                <span style={{ fontSize: '11px', opacity: 0.8 }}>Dashboard Currency: </span>
                <select 
                    className="adm-select" 
                    style={{ width: 100, height: 24, padding: '2px 6px' }}
                    value={displayCurrency} 
                    onChange={e => setDisplayCurrency(e.target.value)}
                >
                    <option value="USD">USD</option>
                    <option value="EUR">EUR</option>
                    <option value="GBP">GBP</option>
                </select>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading Exposure assets...</div>
                ) : mappedExposure.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No exposure assets found.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th>Asset</th>
                                <th className="adm-num">Clients (Units)</th>
                                <th className="adm-num">Coverage (Units)</th>
                                <th className="adm-num">Net Total (Units)</th>
                                <th className="adm-num">Rate ({displayCurrency})</th>
                                <th className="adm-num">Net Total ({displayCurrency})</th>
                                <th className="adm-num">Positive ({displayCurrency})</th>
                            </tr>
                        </thead>
                        <tbody>
                            {mappedExposure.map(d => (
                                <tr key={d.asset}>
                                    <td><strong>{d.asset}</strong></td>
                                    <td className="adm-num">{(d.clients || 0).toLocaleString('en-US', { maximumFractionDigits: 2 })}</td>
                                    <td className="adm-num">{(d.coverage || 0).toLocaleString('en-US', { maximumFractionDigits: 2 })}</td>
                                    <td className={`adm-num ${d.netTotal === 0 ? '' : d.netTotal > 0 ? 'adm-pos' : 'adm-neg'}`}>
                                        {d.netTotal > 0 ? '+' : ''}{(d.netTotal || 0).toLocaleString('en-US', { maximumFractionDigits: 2 })}
                                    </td>
                                    <td className="adm-num">{d.rate.toLocaleString('en-US', { minimumFractionDigits: 4, maximumFractionDigits: 4 })}</td>
                                    <td className={`adm-num ${d.netTotalConverted >= 0 ? 'adm-pos' : 'adm-neg'}`}>
                                        {d.netTotalConverted >= 0 ? '+' : ''}{d.netTotalConverted.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 })}
                                    </td>
                                    <td className="adm-num adm-pos">
                                        {d.positiveConverted > 0 ? d.positiveConverted.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 }) : '0.00'}
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-positions-margincallpage-tsx'></a>
### 63. `browser/modules/positions/MarginCallPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

export function MarginCallPage(): React.ReactElement {
    const [processedAccounts, setProcessedAccounts] = React.useState<any[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);
    const [filterRiskOnly, setFilterRiskOnly] = React.useState(true);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getRiskMarginCalls();
            setProcessedAccounts(data);
        } catch (err: any) {
            setError(err.message || 'Failed to load margin call accounts list.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    // Filter accounts based on checkbox selection
    const filteredAccounts = React.useMemo(() => {
        if (filterRiskOnly) {
            return processedAccounts.filter(acc => acc.status !== 'OK');
        }
        return processedAccounts;
    }, [processedAccounts, filterRiskOnly]);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn" onClick={loadData}>
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div className="adm-toolbar-sep" />
                <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: '11px', cursor: 'pointer' }}>
                    <input 
                        type="checkbox" 
                        checked={filterRiskOnly} 
                        onChange={e => setFilterRiskOnly(e.target.checked)} 
                    />
                    <span>Show accounts under risk only (Margin Call / Stop Out)</span>
                </label>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading margin accounts...</div>
                ) : filteredAccounts.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>
                        {filterRiskOnly ? 'No accounts are currently in Margin Call or Stop Out state.' : 'No accounts found.'}
                    </div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th>Login ID</th>
                                <th>Group</th>
                                <th className="adm-num">Balance</th>
                                <th className="adm-num">Equity</th>
                                <th className="adm-num">Margin</th>
                                <th className="adm-num">Free Margin</th>
                                <th className="adm-num">Margin Level (%)</th>
                                <th className="adm-num">MC / SO Limits</th>
                                <th style={{ textAlign: 'center' }}>Status</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filteredAccounts.map(acc => {
                                const isRisk = acc.status !== 'OK';
                                return (
                                    <tr 
                                        key={acc.login} 
                                        style={{ 
                                            background: acc.colorCode,
                                            transition: 'background 0.2s'
                                        }}
                                    >
                                        <td><strong>{acc.login}</strong></td>
                                        <td>{acc.group_name}</td>
                                        <td className="adm-num">{(acc.balance || 0).toLocaleString('en-US', { minimumFractionDigits: 2 })} {acc.currency}</td>
                                        <td className="adm-num">{(acc.equity || 0).toLocaleString('en-US', { minimumFractionDigits: 2 })} {acc.currency}</td>
                                        <td className="adm-num">{acc.margin > 0 ? `${(acc.margin || 0).toLocaleString('en-US', { minimumFractionDigits: 2 })} ${acc.currency}` : '—'}</td>
                                        <td className="adm-num">{(acc.freeMargin || 0).toLocaleString('en-US', { minimumFractionDigits: 2 })} {acc.currency}</td>
                                        <td className="adm-num">
                                            {acc.margin > 0 ? (
                                                <strong className={acc.status === 'Stop Out' ? 'adm-neg' : acc.status === 'Margin Call' ? 'adm-neg' : 'adm-pos'}>
                                                    {(acc.marginLevel || 0).toFixed(2)}%
                                                </strong>
                                            ) : '—'}
                                        </td>
                                        <td className="adm-num" style={{ fontSize: '10.5px', opacity: 0.8 }}>
                                            {acc.marginCallLevel}% / {acc.stopOutLevel}%
                                        </td>
                                        <td style={{ textAlign: 'center' }}>
                                            {isRisk ? (
                                                <span 
                                                    className={`adm-tag`}
                                                    style={{ 
                                                        background: acc.status === 'Stop Out' ? 'var(--theia-errorForeground)' : '#f39c12',
                                                        color: '#fff',
                                                        fontWeight: 'bold',
                                                        padding: '2px 8px',
                                                        borderRadius: '3px'
                                                    }}
                                                >
                                                    {acc.status.toUpperCase()}
                                                </span>
                                            ) : (
                                                <span style={{ opacity: 0.6 }}>OK</span>
                                            )}
                                        </td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-positions-positionspage-tsx'></a>
### 63. `browser/modules/positions/PositionsPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

interface Position {
    ticket: number;
    login: number;
    symbol: string;
    action: number; // 0 = Buy, 1 = Sell
    volume: number;
    price_open: number;
    price_current?: number;
    price?: number; // for deals
    price_sl: number;
    price_tp: number;
    profit: number;
    storage: number; // swap
    time_create?: string;
    timestamp?: string; // for deals
    entry?: number; // for deals (0 = In, 1 = Out, 2 = In/Out)
}

interface Props { view: 'open' | 'history'; }

export function PositionsPage({ view }: Props): React.ReactElement {
    const [positions, setPositions] = React.useState<Position[]>([]);
    const [sel, setSel] = React.useState<number | null>(null);
    const [filter, setFilter] = React.useState('');
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            if (view === 'open') {
                const data = await API.getPositions();
                setPositions(data);
            } else {
                // For history, list deals
                const data = await API.getDeals();
                setPositions(data);
            }
        } catch (err: any) {
            setError(err.message || 'Failed to fetch positions/deals.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, [view]);

    const filtered = positions.filter(p =>
        String(p.login).includes(filter) ||
        p.symbol.toLowerCase().includes(filter.toLowerCase()) ||
        String(p.ticket).includes(filter)
    );
    const totalProfit = filtered.reduce((s, p) => s + (p.profit || 0), 0);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn" onClick={loadData} title="Reload data">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div className="adm-toolbar-sep" />
                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input className="adm-search" placeholder="Filter by login, symbol, ticket..." value={filter} onChange={e => setFilter(e.target.value)} />
                </div>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading data...</div>
                ) : filtered.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No records found.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            {view === 'open' ? (
                                <tr>
                                    <th>Ticket</th><th>Login</th><th>Symbol</th><th>Type</th>
                                    <th>Volume</th><th>Open Price</th><th>Current Price</th>
                                    <th>S/L</th><th>T/P</th><th>Float Profit</th><th>Swap</th>
                                    <th>Open Time</th>
                                </tr>
                            ) : (
                                <tr>
                                    <th>Ticket</th><th>Order Ticket</th><th>Login</th><th>Symbol</th><th>Action</th><th>Entry</th>
                                    <th>Volume</th><th>Execution Price</th><th>Realized Profit</th><th>Swap</th><th>Commission</th>
                                    <th>Timestamp</th>
                                </tr>
                            )}
                        </thead>
                        <tbody>
                            {filtered.map(p => {
                                const isBuy = p.action === 0;
                                const typeStr = isBuy ? 'BUY' : 'SELL';
                                const ticketId = p.ticket;

                                if (view === 'open') {
                                    return (
                                        <tr key={ticketId} className={sel === ticketId ? 'selected' : ''} onClick={() => setSel(ticketId)}>
                                            <td><strong>{p.ticket}</strong></td>
                                            <td>{p.login}</td>
                                            <td><strong>{p.symbol}</strong></td>
                                            <td><span className={`adm-side-badge ${typeStr.toLowerCase()}`}>{typeStr}</span></td>
                                            <td>{(p.volume || 0).toFixed(2)}</td>
                                            <td className="adm-num">{(p.price_open || 0).toFixed(5)}</td>
                                            <td className="adm-num">{(p.price_current || 0).toFixed(5)}</td>
                                            <td className="adm-num">{p.price_sl || '—'}</td>
                                            <td className="adm-num">{p.price_tp || '—'}</td>
                                            <td className={`adm-num ${(p.profit || 0) >= 0 ? 'adm-pos' : 'adm-neg'}`}>{(p.profit || 0) >= 0 ? '+' : ''}{(p.profit || 0).toFixed(2)}</td>
                                            <td className="adm-num">{(p.storage || 0).toFixed(2)}</td>
                                            <td>{p.time_create || '—'}</td>
                                        </tr>
                                    );
                                } else {
                                    // Deal history format
                                    const entryStr = p.entry === 0 ? 'IN' : p.entry === 1 ? 'OUT' : 'IN/OUT';
                                    return (
                                        <tr key={ticketId} className={sel === ticketId ? 'selected' : ''} onClick={() => setSel(ticketId)}>
                                            <td><strong>{p.ticket}</strong></td>
                                            <td>{p.order_ticket || '—'}</td>
                                            <td>{p.login}</td>
                                            <td><strong>{p.symbol}</strong></td>
                                            <td><span className={`adm-side-badge ${typeStr.toLowerCase()}`}>{typeStr}</span></td>
                                            <td><span className="adm-tag">{entryStr}</span></td>
                                            <td>{(p.volume || 0).toFixed(2)}</td>
                                            <td className="adm-num">{(p.price || 0).toFixed(5)}</td>
                                            <td className={`adm-num ${(p.profit || 0) >= 0 ? 'adm-pos' : 'adm-neg'}`}>{(p.profit || 0) >= 0 ? '+' : ''}{(p.profit || 0).toFixed(2)}</td>
                                            <td className="adm-num">{(p.storage || 0).toFixed(2)}</td>
                                            <td className="adm-num adm-neg">{(p.commission || 0).toFixed(2)}</td>
                                            <td>{p.timestamp || '—'}</td>
                                        </tr>
                                    );
                                }
                            })}
                        </tbody>
                    </table>
                )}
            </div>

            <div className="adm-statusbar">
                <span>{view === 'open' ? 'Open Positions' : 'Closed Deals'}: {filtered.length}</span>
                <span className="adm-sep">|</span>
                <span className={totalProfit >= 0 ? 'adm-pos' : 'adm-neg'}>
                    Total {view === 'open' ? 'Float P&L' : 'Realized P&L'}: {totalProfit >= 0 ? '+' : ''}{totalProfit.toFixed(2)} USD
                </span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-positions-summarypage-tsx'></a>
### 63. `browser/modules/positions/SummaryPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

export function SummaryPage(): React.ReactElement {
    const [summaryData, setSummaryData] = React.useState<any[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getRiskSummary();
            setSummaryData(data);
        } catch (err: any) {
            setError(err.message || 'Failed to load summary positions data.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn" onClick={loadData}>
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-table-wrap">
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading Summary positions...</div>
                ) : summaryData.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No summary positions available.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th rowSpan={2}>Symbol</th>
                                <th colSpan={4} style={{ textAlign: 'center', borderBottom: '1px solid var(--theia-widget-border)' }}>Clients Summary</th>
                                <th colSpan={4} style={{ textAlign: 'center', borderBottom: '1px solid var(--theia-widget-border)' }}>Coverage Summary</th>
                                <th rowSpan={2} className="adm-num">Net Vol (Lots)</th>
                                <th rowSpan={2} className="adm-num">Uncovered Profit</th>
                            </tr>
                            <tr>
                                <th className="adm-num">Buy Vol</th>
                                <th className="adm-num">Buy Price</th>
                                <th className="adm-num">Sell Vol</th>
                                <th className="adm-num">Sell Price</th>
                                <th className="adm-num">Buy Vol</th>
                                <th className="adm-num">Buy Price</th>
                                <th className="adm-num">Sell Vol</th>
                                <th className="adm-num">Sell Price</th>
                            </tr>
                        </thead>
                        <tbody>
                            {summaryData.map(d => (
                                <tr key={d.symbol}>
                                    <td><strong>{d.symbol}</strong></td>
                                    <td className="adm-num">{(d.clientBuyVol || 0).toFixed(2)}</td>
                                    <td className="adm-num">{d.clientBuyAvg > 0 ? d.clientBuyAvg.toFixed(5) : '—'}</td>
                                    <td className="adm-num">{(d.clientSellVol || 0).toFixed(2)}</td>
                                    <td className="adm-num">{d.clientSellAvg > 0 ? d.clientSellAvg.toFixed(5) : '—'}</td>
                                    <td className="adm-num">{(d.covBuyVol || 0).toFixed(2)}</td>
                                    <td className="adm-num">{d.covBuyAvg > 0 ? d.covBuyAvg.toFixed(5) : '—'}</td>
                                    <td className="adm-num">{(d.covSellVol || 0).toFixed(2)}</td>
                                    <td className="adm-num">{d.covSellAvg > 0 ? d.covSellAvg.toFixed(5) : '—'}</td>
                                    <td className={`adm-num ${d.netVol === 0 ? '' : d.netVol > 0 ? 'adm-pos' : 'adm-neg'}`}>
                                        {d.netVol > 0 ? '+' : ''}{(d.netVol || 0).toFixed(2)}
                                    </td>
                                    <td className={`adm-num ${d.uncoveredProfit >= 0 ? 'adm-pos' : 'adm-neg'}`}>
                                        {d.uncoveredProfit >= 0 ? '+' : ''}{(d.uncoveredProfit || 0).toFixed(2)} USD
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-routing-routingpage-tsx'></a>
### 63. `browser/modules/routing/RoutingPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';

const ACTION_COLOR: Record<string, string> = {
    INSTANT_EXECUTE: '#27ae60',
    TO_DEALER:       '#9b59b6',
    TO_GATEWAY:      '#3498db',
    REJECT:          '#e74c3c',
};

export function RoutingPage(): React.ReactElement {
    const [rules, setRules] = React.useState<any[]>([]);
    const [gateways, setGateways] = React.useState<any[]>([]);
    const [accounts, setAccounts] = React.useState<any[]>([]);
    const [selected, setSelected] = React.useState<number | null>(null);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);
    
    // Modal states
    const [showModal, setShowModal] = React.useState(false);
    const [modalMode, setModalMode] = React.useState<'create' | 'edit'>('create');
    const [modalTab, setModalTab] = React.useState<'common' | 'dealers'>('common');
    
    const [ruleForm, setRuleForm] = React.useState({
        id: null as number | null,
        name: '',
        is_enabled: true,
        action: 'INSTANT_EXECUTE',
        gateway_id: '',
        delay_seconds: '0',
        match_groups: '',
        match_symbols: '',
        match_accounts: '',
        match_order_types: '',
        match_volume_min: '',
        match_volume_max: ''
    });
    const [modalError, setModalError] = React.useState<string | null>(null);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const rulesData = await API.getRoutingRules();
            setRules(rulesData);
            const gwsData = await API.getGateways();
            setGateways(gwsData);
            const accsData = await API.getAccounts();
            setAccounts(accsData);
        } catch (err: any) {
            setError(err.message || 'Failed to fetch routing rules, gateways, or accounts.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    const toggleRule = async (id: number, currentEnabled: boolean) => {
        setError(null);
        try {
            if (currentEnabled) {
                await API.disableRoutingRule(id);
            } else {
                await API.enableRoutingRule(id);
            }
            await loadData();
        } catch (err: any) {
            setError(err.message || 'Failed to toggle rule state.');
        }
    };

    const handleDelete = async () => {
        if (!selected) return;
        if (!confirm('Are you sure you want to delete this routing rule?')) return;
        setError(null);
        try {
            await API.deleteRoutingRule(selected);
            setSelected(null);
            await loadData();
        } catch (err: any) {
            setError(err.message || 'Failed to delete routing rule.');
        }
    };

    const moveUp = async (id: number) => {
        const idx = rules.findIndex(r => r.id === id);
        if (idx <= 0) return;
        
        const newOrderIds = rules.map(r => r.id);
        [newOrderIds[idx - 1], newOrderIds[idx]] = [newOrderIds[idx], newOrderIds[idx - 1]];
        
        setError(null);
        try {
            await API.reorderRoutingRules(newOrderIds);
            await loadData();
        } catch (err: any) {
            setError(err.message || 'Failed to reorder rules.');
        }
    };

    const moveDown = async (id: number) => {
        const idx = rules.findIndex(r => r.id === id);
        if (idx < 0 || idx >= rules.length - 1) return;
        
        const newOrderIds = rules.map(r => r.id);
        [newOrderIds[idx], newOrderIds[idx + 1]] = [newOrderIds[idx + 1], newOrderIds[idx]];
        
        setError(null);
        try {
            await API.reorderRoutingRules(newOrderIds);
            await loadData();
        } catch (err: any) {
            setError(err.message || 'Failed to reorder rules.');
        }
    };

    const openCreateModal = () => {
        setModalMode('create');
        setModalTab('common');
        setRuleForm({
            id: null,
            name: '',
            is_enabled: true,
            action: 'INSTANT_EXECUTE',
            gateway_id: '',
            delay_seconds: '0',
            match_groups: '',
            match_symbols: '',
            match_accounts: '',
            match_order_types: '',
            match_volume_min: '',
            match_volume_max: ''
        });
        setModalError(null);
        setShowModal(true);
    };

    const openEditModal = (r: any) => {
        setModalMode('edit');
        setModalTab('common');
        setRuleForm({
            id: r.id,
            name: r.name,
            is_enabled: r.is_enabled,
            action: r.action,
            gateway_id: r.gateway_id ? String(r.gateway_id) : '',
            delay_seconds: String(r.delay_seconds || 0),
            match_groups: r.match_groups ? r.match_groups.join(', ') : '',
            match_symbols: r.match_symbols ? r.match_symbols.join(', ') : '',
            match_accounts: r.match_accounts ? r.match_accounts.join(', ') : '',
            match_order_types: r.match_order_types ? r.match_order_types.join(', ') : '',
            match_volume_min: r.match_volume_min !== null ? String(r.match_volume_min) : '',
            match_volume_max: r.match_volume_max !== null ? String(r.match_volume_max) : ''
        });
        setModalError(null);
        setShowModal(true);
    };

    const handleSubmitRule = async (e: React.FormEvent) => {
        e.preventDefault();
        setModalError(null);
        try {
            const currentRule = rules.find(r => r.id === ruleForm.id);
            const payload = {
                name: ruleForm.name,
                priority: modalMode === 'create' ? rules.length + 1 : (currentRule ? currentRule.priority : 1),
                is_enabled: ruleForm.is_enabled,
                action: ruleForm.action,
                gateway_id: ruleForm.gateway_id ? parseInt(ruleForm.gateway_id) : undefined,
                delay_seconds: parseInt(ruleForm.delay_seconds) || 0,
                match_groups: ruleForm.match_groups ? ruleForm.match_groups.split(',').map(s => s.trim()).filter(Boolean) : undefined,
                match_symbols: ruleForm.match_symbols ? ruleForm.match_symbols.split(',').map(s => s.trim()).filter(Boolean) : undefined,
                match_accounts: ruleForm.match_accounts ? ruleForm.match_accounts.split(',').map(s => s.trim()).filter(Boolean) : undefined,
                match_order_types: ruleForm.match_order_types ? ruleForm.match_order_types.split(',').map(s => s.trim()).filter(Boolean) : undefined,
                match_volume_min: ruleForm.match_volume_min ? parseFloat(ruleForm.match_volume_min) : undefined,
                match_volume_max: ruleForm.match_volume_max ? parseFloat(ruleForm.match_volume_max) : undefined,
            };

            if (modalMode === 'create') {
                await API.createRoutingRule(payload);
            } else {
                await API.updateRoutingRule(ruleForm.id!, payload);
            }
            setShowModal(false);
            await loadData();
        } catch (err: any) {
            setModalError(err.message || 'Failed to save routing rule.');
        }
    };

    const selectedRule = rules.find(r => r.id === selected);

    // Selected gateway info inside the Dealers tab
    const ruleGateway = gateways.find(g => String(g.id) === ruleForm.gateway_id);
    const ruleManager = accounts.find(a => String(a.login) === ruleForm.gateway_id);

    return (
        <div className="adm-page">
            <div className="adm-toolbar">
                <button className="adm-btn adm-btn-primary" onClick={openCreateModal}>
                    <i className="codicon codicon-add" /> Add Rule
                </button>
                <button className="adm-btn" disabled={!selectedRule} onClick={() => selectedRule && openEditModal(selectedRule)}>
                    <i className="codicon codicon-edit" /> Edit Rule
                </button>
                <button className="adm-btn adm-btn-danger" disabled={selected === null} onClick={handleDelete}>
                    <i className="codicon codicon-trash" /> Delete
                </button>
                <div className="adm-toolbar-sep" />
                <button className="adm-btn" disabled={selected === null || rules.findIndex(r => r.id === selected) === 0} onClick={() => selected && moveUp(selected)}>
                    <i className="codicon codicon-arrow-up" /> Move Up
                </button>
                <button className="adm-btn" disabled={selected === null || rules.findIndex(r => r.id === selected) === rules.length - 1} onClick={() => selected && moveDown(selected)}>
                    <i className="codicon codicon-arrow-down" /> Move Down
                </button>
                <div className="adm-toolbar-sep" />
                <button className="adm-btn" onClick={loadData} title="Reload data">
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
                <div style={{ marginLeft: 'auto', display: 'flex', alignItems: 'center', gap: 6 }}>
                    <a 
                        href="file:///c:/Users/DELL/Downloads/server3/MT5-Administrator/MetaTrader-5-Trading-Platform/Platform-Setup/Routing.md" 
                        target="_blank" 
                        rel="noreferrer"
                        className="adm-btn"
                        style={{ display: 'inline-flex', alignItems: 'center', gap: 4, textDecoration: 'none', color: 'inherit' }}
                    >
                        <i className="codicon codicon-book" /> Routing Guide
                    </a>
                </div>
            </div>

            <div className="adm-hint">
                <i className="codicon codicon-info" />
                Rules are executed <strong>top-to-bottom</strong> based on priority. First matching rule wins. Double-click to Edit.
            </div>

            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            <div className="adm-split-view">
                <div className="adm-table-wrap" style={{ flex: selectedRule ? '0 0 55%' : '1' }}>
                    {loading ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading routing rules...</div>
                    ) : rules.length === 0 ? (
                        <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>No routing rules configured. Create one to route orders.</div>
                    ) : (
                        <table className="adm-table">
                            <thead>
                                <tr>
                                    <th>Priority</th>
                                    <th>Enabled</th>
                                    <th>Rule Name</th>
                                    <th>Action</th>
                                    <th>Match Specs</th>
                                    <th>Gateway Route</th>
                                </tr>
                            </thead>
                            <tbody>
                                {rules.map((r, idx) => (
                                    <tr 
                                        key={r.id} 
                                        className={`${selected === r.id ? 'selected' : ''} ${!r.is_enabled ? 'adm-row-disabled' : ''}`} 
                                        onClick={() => setSelected(r.id)}
                                        onDoubleClick={() => openEditModal(r)}
                                    >
                                        <td style={{ opacity: 0.5 }}>{idx + 1}</td>
                                        <td>
                                            <button
                                                className={`adm-toggle ${r.is_enabled ? 'on' : 'off'}`}
                                                onClick={e => { e.stopPropagation(); toggleRule(r.id, r.is_enabled); }}
                                            >
                                                {r.is_enabled ? '✓' : '✗'}
                                            </button>
                                        </td>
                                        <td><strong>{r.name}</strong></td>
                                        <td>
                                            <span className="adm-tag" style={{ color: ACTION_COLOR[r.action] || '#aaa', border: `1px solid ${(ACTION_COLOR[r.action] || '#aaa')}55` }}>
                                                {r.action}
                                            </span>
                                        </td>
                                        <td>
                                            {r.match_symbols.length > 0 && <span className="adm-condition-chip" title="Symbols">Sym: {r.match_symbols.join(',')}</span>}
                                            {r.match_groups.length > 0 && <span className="adm-condition-chip" title="Groups">Grp: {r.match_groups.join(',')}</span>}
                                            {r.match_accounts.length > 0 && <span className="adm-condition-chip" title="Accounts">Acc: {r.match_accounts.join(',')}</span>}
                                            {r.match_volume_min !== null && <span className="adm-condition-chip">Min Vol: {r.match_volume_min}</span>}
                                            {r.match_volume_max !== null && <span className="adm-condition-chip">Max Vol: {r.match_volume_max}</span>}
                                            {r.match_symbols.length === 0 && r.match_groups.length === 0 && r.match_accounts.length === 0 && r.match_volume_min === null && r.match_volume_max === null && (
                                                <span style={{ opacity: 0.5 }}>— Catchall —</span>
                                            )}
                                        </td>
                                        <td>
                                            {r.gateway_id ? (
                                                <strong>{gateways.find(g => g.id === r.gateway_id)?.name || `Gateway #${r.gateway_id}`}</strong>
                                            ) : (
                                                <span style={{ opacity: 0.5 }}>—</span>
                                            )}
                                        </td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    )}
                </div>

                {selectedRule && (
                    <div className="adm-detail-panel">
                        <div className="adm-detail-header">
                            <span>Rule Detail: {selectedRule.name}</span>
                            <button className="adm-icon-btn" onClick={() => setSelected(null)}><i className="codicon codicon-close" /></button>
                        </div>
                        <div className="adm-detail-body">
                            <div className="adm-detail-section">General</div>
                            <div className="adm-kv"><span>Name</span><strong>{selectedRule.name}</strong></div>
                            <div className="adm-kv"><span>Priority</span><span>{rules.findIndex(r => r.id === selectedRule.id) + 1}</span></div>
                            <div className="adm-kv"><span>Action</span><span style={{ color: ACTION_COLOR[selectedRule.action] }}>{selectedRule.action}</span></div>
                            <div className="adm-kv">
                                <span>Gateway Route</span>
                                <strong>{gateways.find(g => g.id === selectedRule.gateway_id)?.name || 'Local Matching (B-Book)'}</strong>
                            </div>
                            <div className="adm-kv"><span>Delay Seconds</span><span>{selectedRule.delay_seconds || 0} s</span></div>

                            <div className="adm-detail-section">Filter Rules</div>
                            <div className="adm-kv"><span>Symbols</span><span>{selectedRule.match_symbols.length > 0 ? selectedRule.match_symbols.join(', ') : 'All'}</span></div>
                            <div className="adm-kv"><span>Groups</span><span>{selectedRule.match_groups.length > 0 ? selectedRule.match_groups.join(', ') : 'All'}</span></div>
                            <div className="adm-kv"><span>Accounts</span><span>{selectedRule.match_accounts && selectedRule.match_accounts.length > 0 ? selectedRule.match_accounts.join(', ') : 'All'}</span></div>
                            <div className="adm-kv"><span>Order Types</span><span>{selectedRule.match_order_types.length > 0 ? selectedRule.match_order_types.join(', ') : 'All'}</span></div>
                            <div className="adm-kv"><span>Min Vol</span><span>{selectedRule.match_volume_min !== null ? selectedRule.match_volume_min : 'Any'}</span></div>
                            <div className="adm-kv"><span>Max Vol</span><span>{selectedRule.match_volume_max !== null ? selectedRule.match_volume_max : 'Any'}</span></div>
                        </div>
                    </div>
                )}
            </div>

            {showModal && (
                <div className="adm-modal-overlay" onClick={() => setShowModal(false)}>
                    <form 
                        className="adm-modal" 
                        style={{ width: 750, height: '65vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }} 
                        onClick={e => e.stopPropagation()} 
                        onSubmit={handleSubmitRule}
                    >
                        <div className="adm-modal-header">
                            <h2>
                                <i className="codicon codicon-split-horizontal" style={{ marginRight: 8, color: '#3498db' }} />
                                {modalMode === 'create' ? 'Add Routing Rule' : `Edit Routing Rule — ${ruleForm.name}`}
                            </h2>
                            <button type="button" className="adm-modal-close" onClick={() => setShowModal(false)}>×</button>
                        </div>
                        
                        {/* Modal tabs */}
                        <div className="adm-tabs" style={{ padding: '0 16px', borderBottom: '1px solid var(--theia-border)' }}>
                            <button 
                                type="button" 
                                className={`adm-tab ${modalTab === 'common' ? 'active' : ''}`}
                                onClick={() => setModalTab('common')}
                            >
                                Common
                            </button>
                            <button 
                                type="button" 
                                className={`adm-tab ${modalTab === 'dealers' ? 'active' : ''}`}
                                onClick={() => setModalTab('dealers')}
                            >
                                Dealers
                            </button>
                        </div>

                        <div className="adm-modal-body" style={{ flex: 1, overflowY: 'auto', padding: '16px' }}>
                            {modalError && (
                                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 16px 0' }}>
                                    <i className="codicon codicon-error" /> {modalError}
                                </div>
                            )}

                            {modalTab === 'common' ? (
                                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px' }}>
                                    
                                    {/* Left Column - General Setup */}
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                        <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2 }}>
                                            General Properties
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Rule Name</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} required placeholder="e.g. Route EURUSD to LP" value={ruleForm.name} onChange={e => setRuleForm({ ...ruleForm, name: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Execution Action</label>
                                            <select className="adm-select" style={{ width: '100%', height: 20 }} value={ruleForm.action} onChange={e => setRuleForm({ ...ruleForm, action: e.target.value })}>
                                                <option value="INSTANT_EXECUTE">Instant Execute (B-Book)</option>
                                                <option value="TO_GATEWAY">To Gateway (A-Book)</option>
                                                <option value="TO_DEALER">To Dealer Queue (Manual confirmation)</option>
                                                <option value="REJECT">Reject (Block Execution)</option>
                                            </select>
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Delay Seconds</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} type="number" placeholder="0" value={ruleForm.delay_seconds} onChange={e => setRuleForm({ ...ruleForm, delay_seconds: e.target.value })} />
                                        </div>
                                        <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', marginTop: 8, fontSize: 11 }}>
                                            <input type="checkbox" checked={ruleForm.is_enabled} onChange={e => setRuleForm({ ...ruleForm, is_enabled: e.target.checked })} />
                                            Enable this rule
                                        </label>
                                    </div>

                                    {/* Right Column - Filtering criteria */}
                                    <div style={{ display: 'flex', flexDirection: 'column', gap: 10 }}>
                                        <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2 }}>
                                            Filtering Criteria (Comma-separated)
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Match Groups</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} placeholder="e.g. demo_group, real_group" value={ruleForm.match_groups} onChange={e => setRuleForm({ ...ruleForm, match_groups: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Match Symbols</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} placeholder="e.g. EURUSD, GBPUSD" value={ruleForm.match_symbols} onChange={e => setRuleForm({ ...ruleForm, match_symbols: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Match Accounts (Logins)</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} placeholder="e.g. 50080, 50081" value={ruleForm.match_accounts} onChange={e => setRuleForm({ ...ruleForm, match_accounts: e.target.value })} />
                                        </div>
                                        <div className="adm-form-row">
                                            <label>Match Order Types</label>
                                            <input className="adm-input" style={{ width: '100%', height: 20 }} placeholder="e.g. BUY, SELL" value={ruleForm.match_order_types} onChange={e => setRuleForm({ ...ruleForm, match_order_types: e.target.value })} />
                                        </div>
                                        <div style={{ display: 'flex', gap: 8 }}>
                                            <div className="adm-form-row" style={{ flex: 1 }}>
                                                <label>Min Volume</label>
                                                <input className="adm-input" style={{ width: '100%', height: 20 }} type="number" step="0.01" placeholder="Any" value={ruleForm.match_volume_min} onChange={e => setRuleForm({ ...ruleForm, match_volume_min: e.target.value })} />
                                            </div>
                                            <div className="adm-form-row" style={{ flex: 1 }}>
                                                <label>Max Volume</label>
                                                <input className="adm-input" style={{ width: '100%', height: 20 }} type="number" step="0.01" placeholder="Any" value={ruleForm.match_volume_max} onChange={e => setRuleForm({ ...ruleForm, match_volume_max: e.target.value })} />
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
                                    <div style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)', borderBottom: '1px solid var(--theia-border)', paddingBottom: 4 }}>
                                        Configure Dealers (Managers) or ECN Gateways associated with this routing rule.
                                    </div>

                                    {/* Action execution warning/helper */}
                                    {ruleForm.action !== 'TO_DEALER' && ruleForm.action !== 'TO_GATEWAY' ? (
                                        <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-infoBackground)', color: 'var(--theia-inputValidation-infoForeground)' }}>
                                            <i className="codicon codicon-info" /> The Dealers/Gateways list is only active when the rule action is set to <strong>Process to dealers</strong> or <strong>To Gateway (A-Book)</strong>.
                                        </div>
                                    ) : ruleForm.action === 'TO_DEALER' ? (
                                        <>
                                            {/* Dealers Table */}
                                            <div style={{ border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                                <table className="adm-table" style={{ margin: 0 }}>
                                                    <thead>
                                                        <tr>
                                                            <th>Manager Login</th>
                                                            <th>Group Name</th>
                                                            <th>Balance</th>
                                                            <th>Leverage</th>
                                                            <th>Status</th>
                                                            <th style={{ width: 80 }}>Action</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        {ruleManager ? (
                                                            <tr>
                                                                <td><strong>{ruleManager.login}</strong></td>
                                                                <td><strong>{ruleManager.group_name}</strong></td>
                                                                <td>{parseFloat(ruleManager.balance || 0).toFixed(2)} USD</td>
                                                                <td>1:{ruleManager.leverage}</td>
                                                                <td>
                                                                    <span className="adm-status-dot online" style={{ marginRight: 6 }} />
                                                                    Dealing
                                                                </td>
                                                                <td>
                                                                    <button 
                                                                        type="button" 
                                                                        className="adm-btn" 
                                                                        style={{ padding: '2px 6px', color: 'var(--theia-errorForeground)' }}
                                                                        onClick={() => setRuleForm({ ...ruleForm, gateway_id: '' })}
                                                                    >
                                                                        <i className="codicon codicon-trash" /> Delete
                                                                    </button>
                                                                </td>
                                                            </tr>
                                                        ) : (
                                                            <tr>
                                                                <td colSpan={6} style={{ textAlign: 'center', opacity: 0.6, padding: 16 }}>
                                                                    No dealer accounts currently assigned. Use the selection below to assign one.
                                                                </td>
                                                            </tr>
                                                        )}
                                                    </tbody>
                                                </table>
                                            </div>

                                            {/* Dealer assign selector */}
                                            {!ruleForm.gateway_id && (
                                                <div style={{ display: 'flex', gap: 8, alignItems: 'center', marginTop: 12 }}>
                                                    <span style={{ fontSize: 11 }}>Select Manager Account:</span>
                                                    <select 
                                                        className="adm-select" 
                                                        style={{ width: 260, height: 22 }}
                                                        value="" 
                                                        onChange={e => {
                                                            if (e.target.value) {
                                                                setRuleForm({ ...ruleForm, gateway_id: e.target.value });
                                                            }
                                                        }}
                                                    >
                                                        <option value="">Choose Dealing Manager...</option>
                                                        {accounts.filter(a => a.group_name && a.group_name.toLowerCase().includes('manager')).map(m => (
                                                            <option key={m.login} value={m.login}>
                                                                {m.login} ({m.group_name})
                                                            </option>
                                                        ))}
                                                    </select>
                                                </div>
                                            )}
                                        </>
                                    ) : (
                                        <>
                                            {/* Gateways table */}
                                            <div style={{ border: '1px solid var(--theia-border)', borderRadius: 4 }}>
                                                <table className="adm-table" style={{ margin: 0 }}>
                                                    <thead>
                                                        <tr>
                                                            <th>Dealer/Gateway ID</th>
                                                            <th>Gateway Name</th>
                                                            <th>Type</th>
                                                            <th>Connection Host</th>
                                                            <th>Status</th>
                                                            <th style={{ width: 80 }}>Action</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        {ruleGateway ? (
                                                            <tr>
                                                                <td><strong>{ruleGateway.id}</strong></td>
                                                                <td><strong>{ruleGateway.name}</strong></td>
                                                                <td><span className="adm-tag" style={{ fontSize: 9 }}>{ruleGateway.type}</span></td>
                                                                <td><code className="adm-code">{ruleGateway.host || 'localhost'}</code></td>
                                                                <td>
                                                                    <span className={`adm-status-dot ${ruleGateway.is_active ? 'online' : 'offline'}`} style={{ marginRight: 6 }} />
                                                                    {ruleGateway.is_active ? 'Active' : 'Offline'}
                                                                </td>
                                                                <td>
                                                                    <button 
                                                                        type="button" 
                                                                        className="adm-btn" 
                                                                        style={{ padding: '2px 6px', color: 'var(--theia-errorForeground)' }}
                                                                        onClick={() => setRuleForm({ ...ruleForm, gateway_id: '' })}
                                                                    >
                                                                        <i className="codicon codicon-trash" /> Delete
                                                                    </button>
                                                                </td>
                                                            </tr>
                                                        ) : (
                                                            <tr>
                                                                <td colSpan={6} style={{ textAlign: 'center', opacity: 0.6, padding: 16 }}>
                                                                    No gateways currently assigned. Use the selection below to assign one.
                                                                </td>
                                                            </tr>
                                                        )}
                                                    </tbody>
                                                </table>
                                            </div>

                                            {/* Gateway assign selector */}
                                            {!ruleForm.gateway_id && (
                                                <div style={{ display: 'flex', gap: 8, alignItems: 'center', marginTop: 12 }}>
                                                    <span style={{ fontSize: 11 }}>Select Gateway:</span>
                                                    <select 
                                                        className="adm-select" 
                                                        style={{ width: 220, height: 22 }}
                                                        value="" 
                                                        onChange={e => {
                                                            if (e.target.value) {
                                                                setRuleForm({ ...ruleForm, gateway_id: e.target.value });
                                                            }
                                                        }}
                                                    >
                                                        <option value="">Choose LP Gateway...</option>
                                                        {gateways.map(g => (
                                                            <option key={g.id} value={g.id}>
                                                                {g.name} ({g.type}) — {g.host || 'localhost'}
                                                            </option>
                                                        ))}
                                                    </select>
                                                </div>
                                            )}
                                        </>
                                    )}
                                </div>
                            )}
                        </div>

                        <div className="adm-modal-footer">
                            <button type="submit" className="adm-btn adm-btn-primary">
                                {modalMode === 'create' ? 'Create Rule' : 'Save Changes'}
                            </button>
                            <button type="button" className="adm-btn" onClick={() => setShowModal(false)}>
                                Cancel
                            </button>
                        </div>
                    </form>
                </div>
            )}

            <div className="adm-statusbar">
                <span>Total Rules: {rules.length}</span>
                <span className="adm-sep">|</span>
                <span>Active: {rules.filter(r => r.is_enabled).length}</span>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-allsymbolspage-tsx'></a>
### 63. `browser/modules/symbols/AllSymbolsPage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';
import { getHighestOrderGroup } from './SymbolFolderUtils';
import { SymbolFilterBar } from './SymbolFilterBar';
import { SymbolSettingsModal } from './modal/SymbolSettingsModal';

export function AllSymbolsPage(): React.ReactElement {
    const [symbols, setSymbols] = React.useState<any[]>([]);
    const [filtered, setFiltered] = React.useState<any[]>([]);
    const [selectedRows, setSelectedRows] = React.useState<string[]>([]);
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Modal state
    const [showSettingsModal, setShowSettingsModal] = React.useState(false);
    const [settingsSymbol, setSettingsSymbol] = React.useState<string | null>(null);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getSymbols();
            // Filter out dummy folders
            const validSymbols = data.filter((s: any) => !s.symbol.endsWith('.dummy'));
            setSymbols(validSymbols);
            setFiltered(validSymbols);
        } catch (err: any) {
            setError(err.message || 'Failed to load symbols.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    // Selection handlers
    const handleSelectRow = (symbol: string, e: React.MouseEvent) => {
        if (e.ctrlKey || e.metaKey) {
            if (selectedRows.includes(symbol)) {
                setSelectedRows(prev => prev.filter(r => r !== symbol));
            } else {
                setSelectedRows(prev => [...prev, symbol]);
            }
        } else if (e.shiftKey && selectedRows.length > 0) {
            const last = selectedRows[selectedRows.length - 1];
            const lastIdx = filtered.findIndex(r => r.symbol === last);
            const currIdx = filtered.findIndex(r => r.symbol === symbol);
            if (lastIdx !== -1 && currIdx !== -1) {
                const start = Math.min(lastIdx, currIdx);
                const end = Math.max(lastIdx, currIdx);
                const range = filtered.slice(start, end + 1).map(r => r.symbol);
                setSelectedRows(prev => Array.from(new Set([...prev, ...range])));
            }
        } else {
            setSelectedRows([symbol]);
        }
    };

    const handleEdit = (name?: string) => {
        const target = name || selectedRows[0];
        if (!target) return;
        setSettingsSymbol(target);
        setShowSettingsModal(true);
    };

    const handleFilterApplied = (filteredList: any[]) => {
        setFiltered(filteredList);
        setSelectedRows([]);
    };

    const isSingleSelected = selectedRows.length === 1;

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            {/* Filter controls */}
            <SymbolFilterBar 
                symbols={symbols} 
                onFilterApplied={handleFilterApplied} 
            />

            {/* Toolbar for flat list operations */}
            <div className="adm-toolbar" style={{ borderBottom: 'none', padding: '4px 12px' }}>
                <button type="button" className="adm-btn" disabled={!isSingleSelected} onClick={() => handleEdit()}>
                    <i className="codicon codicon-edit" /> Edit Selected Symbol
                </button>
                <button type="button" className="adm-btn" onClick={loadData}>
                    <i className="codicon codicon-refresh" /> Refresh
                </button>
            </div>

            {/* Error notifications */}
            {error && (
                <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '10px 16px' }}>
                    <i className="codicon codicon-error" /> {error}
                </div>
            )}

            {/* Flat Table */}
            <div className="adm-table-wrap" style={{ flex: 1, overflowY: 'auto' }}>
                {loading ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.7 }}>Loading all symbols...</div>
                ) : filtered.length === 0 ? (
                    <div style={{ padding: 20, textAlign: 'center', opacity: 0.6 }}>No symbols found matching active search parameters.</div>
                ) : (
                    <table className="adm-table">
                        <thead>
                            <tr>
                                <th>Symbol Path Name</th>
                                <th>Type (Highest Group)</th>
                                <th>Execution Mode</th>
                                <th>Digits</th>
                            </tr>
                        </thead>
                        <tbody>
                            {filtered.map(s => {
                                const isSelected = selectedRows.includes(s.symbol);
                                
                                let settings: any = {};
                                if (s.settings_json) {
                                    try { settings = JSON.parse(s.settings_json); } catch {}
                                }
                                
                                const highestGroup = getHighestOrderGroup(s.symbol) || 'Root';
                                const execMode = settings.execution_mode || 'Instant';
                                const digitsVal = s.digits !== undefined ? s.digits : 5;

                                return (
                                    <tr 
                                        key={s.symbol}
                                        className={isSelected ? 'selected' : ''}
                                        onClick={e => handleSelectRow(s.symbol, e)}
                                        onDoubleClick={() => handleEdit(s.symbol)}
                                    >
                                        <td>
                                            <i className="codicon codicon-graph" style={{ color: '#2ecc71', marginRight: 6 }} />
                                            <strong>{s.symbol}</strong>
                                        </td>
                                        <td>{highestGroup}</td>
                                        <td>
                                            <span className="adm-tag">{execMode}</span>
                                        </td>
                                        <td>{digitsVal}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                )}
            </div>

            {/* Status bar */}
            <div className="adm-statusbar">
                <span>Matching symbols: {filtered.length} of {symbols.length}</span>
                {selectedRows.length > 0 && (
                    <>
                        <span className="adm-sep">|</span>
                        <span>Selected: {selectedRows.length}</span>
                    </>
                )}
            </div>

            {/* Settings Modal */}
            {showSettingsModal && (
                <SymbolSettingsModal 
                    symbolName={settingsSymbol}
                    onClose={() => setShowSettingsModal(false)}
                    onSaved={loadData}
                />
            )}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolfilterbar-tsx'></a>
### 63. `browser/modules/symbols/SymbolFilterBar.tsx`

```tsx
import * as React from 'react';

interface SymbolFilterBarProps {
    symbols: any[];
    onFilterApplied: (filtered: any[]) => void;
}

export function SymbolFilterBar({ symbols, onFilterApplied }: SymbolFilterBarProps): React.ReactElement {
    const [filterQuery, setFilterQuery] = React.useState('');

    const matchPattern = (name: string, pattern: string): boolean => {
        // Escape special chars except *
        const escaped = pattern.replace(/[-\/\{\}\(\)\+\?\.\\\^\$\|]/g, '\\$&');
        const wild = escaped.replace(/\*/g, '.*');
        const regex = new RegExp(`^${wild}$`, 'i');
        // Extract the instrument name (last segment) or match full name
        const lastSegment = name.split('\\').pop() || name;
        return regex.test(lastSegment) || regex.test(name);
    };

    const handleApplyFilter = () => {
        if (!filterQuery.trim()) {
            onFilterApplied(symbols);
            return;
        }

        const parts = filterQuery.split(',').map(p => p.trim()).filter(Boolean);
        const positivePatterns = parts.filter(p => !p.startsWith('!'));
        const negativePatterns = parts.filter(p => p.startsWith('!')).map(p => p.substring(1));

        const filtered = symbols.filter(s => {
            // Must match at least one positive pattern (if any are specified)
            let isPositiveMatch = positivePatterns.length === 0;
            for (const p of positivePatterns) {
                if (matchPattern(s.symbol, p)) {
                    isPositiveMatch = true;
                    break;
                }
            }

            // Must NOT match any negative patterns
            let isNegativeMatch = false;
            for (const p of negativePatterns) {
                if (matchPattern(s.symbol, p)) {
                    isNegativeMatch = true;
                    break;
                }
            }

            return isPositiveMatch && !isNegativeMatch;
        });

        onFilterApplied(filtered);
    };

    const handleKeyDown = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter') {
            handleApplyFilter();
        }
    };

    return (
        <div className="adm-toolbar" style={{ borderBottom: '1px solid var(--theia-border)', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', display: 'flex', alignItems: 'center', gap: 12 }}>
            <div style={{ fontSize: 11, fontWeight: '600', color: 'var(--theia-descriptionForeground)', whiteSpace: 'nowrap' }}>
                Filter Query:
            </div>
            <div style={{ flex: 1, display: 'flex', gap: 8 }}>
                <input 
                    className="adm-input" 
                    style={{ flex: 1, fontSize: 11, padding: '3px 8px', height: 24 }}
                    placeholder="e.g. EUR*, *USD, !GBPUSD" 
                    value={filterQuery}
                    onChange={e => setFilterQuery(e.target.value)}
                    onKeyDown={handleKeyDown}
                />
                <button 
                    type="button" 
                    className="adm-btn adm-btn-primary" 
                    style={{ padding: '0 12px', height: 24, fontSize: 11 }}
                    onClick={handleApplyFilter}
                >
                    Apply Filter
                </button>
                {filterQuery && (
                    <button 
                        type="button" 
                        className="adm-btn" 
                        style={{ padding: '0 8px', height: 24, fontSize: 11 }}
                        onClick={() => {
                            setFilterQuery('');
                            onFilterApplied(symbols);
                        }}
                    >
                        Clear
                    </button>
                )}
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolfolderutils-ts'></a>
### 63. `browser/modules/symbols/SymbolFolderUtils.ts`

```typescript
/**
 * Pure helper utilities for validation and segmentation of MT5 symbol folder paths and names.
 */

/**
 * Validates a folder or group name based on MT5 rules.
 * Allowed characters: letters, digits, '.', '_', '&', '#'.
 * Blocked characters: < > : " / | ? * and comma.
 */
export function validateFolderName(name: string): string | null {
    if (!name || !name.trim()) {
        return 'Folder name cannot be empty.';
    }
    // Check if it contains invalid characters
    const invalidRegex = /[<>:"/\\|?*,]/;
    if (invalidRegex.test(name)) {
        return 'Folder name cannot contain special characters like <, >, :, ", /, \\, |, ?, * or comma.';
    }
    // Ensure only letters, digits, dot, underscore, ampersand, and hash are used
    const allowedRegex = /^[a-zA-Z0-9._&#\s-]+$/;
    if (!allowedRegex.test(name)) {
        return 'Folder name contains invalid characters. Only letters, numbers, spaces, and . _ & # - are allowed.';
    }
    return null;
}

/**
 * Validates a symbol name.
 * Rules: No leading/trailing spaces, must not contain invalid characters.
 */
export function validateSymbolName(name: string, existingSymbols: string[]): string | null {
    const trimmed = name.trim();
    if (!trimmed) {
        return 'Symbol name cannot be empty.';
    }
    if (name !== trimmed) {
        return 'Symbol name cannot contain leading or trailing whitespace.';
    }
    const invalidRegex = /[<>:"/\\|?*,]/;
    if (invalidRegex.test(trimmed)) {
        return 'Symbol name cannot contain special characters like <, >, :, ", /, \\, |, ?, * or comma.';
    }
    const allowedRegex = /^[a-zA-Z0-9._&#-]+$/;
    if (!allowedRegex.test(trimmed)) {
        return 'Symbol name can only contain alphanumeric characters and . _ & # -';
    }
    // Case insensitivity checks to prevent Apple vs APPLE duplicate issues
    const matchCaseInsensitive = existingSymbols.some(
        s => s.toLowerCase() === trimmed.toLowerCase()
    );
    if (matchCaseInsensitive) {
        return `A symbol with the name "${trimmed}" (or a case-variant like "${trimmed.toUpperCase()}") already exists.`;
    }
    return null;
}

/**
 * Splits a full symbol path (e.g. "Forex\\Majors\\EURUSD") into folder segments.
 */
export function splitSymbolPath(fullPath: string): string[] {
    return fullPath.split('\\').map(p => p.trim()).filter(Boolean);
}

/**
 * Extracts highest order group/type from a symbol path name (e.g. "Forex\\Majors\\EURUSD" -> "Forex").
 */
export function getHighestOrderGroup(fullPath: string): string {
    const parts = splitSymbolPath(fullPath);
    return parts.length > 0 ? parts[0] : '';
}

```

---

<a id='browser-modules-symbols-symbolscontextmenu-tsx'></a>
### 63. `browser/modules/symbols/SymbolsContextMenu.tsx`

```tsx
import * as React from 'react';

interface SymbolsContextMenuProps {
    menu: { x: number, y: number, target: string, type: 'folder' | 'symbol' | 'root' };
    isSingleSymbolSelected: boolean;
    onClose: () => void;
    onAddSymbol: () => void;
    onAddFolder: () => void;
    onEdit: () => void;
    onDelete: () => void;
    onSort: () => void;
    onImportServer: () => void;
}

export function SymbolsContextMenu({ 
    menu, 
    isSingleSymbolSelected, 
    onClose, 
    onAddSymbol, 
    onAddFolder, 
    onEdit, 
    onDelete, 
    onSort, 
    onImportServer 
}: SymbolsContextMenuProps): React.ReactElement {
    React.useEffect(() => {
        const handleOutsideClick = () => onClose();
        window.addEventListener('click', handleOutsideClick);
        return () => window.removeEventListener('click', handleOutsideClick);
    }, [onClose]);

    const handleAction = (actionFn: () => void) => {
        actionFn();
        onClose();
    };

    return (
        <div 
            className="adm-context-menu"
            style={{ top: menu.y, left: menu.x }}
            onClick={e => e.stopPropagation()}
        >
            <button type="button" className="adm-context-item" onClick={() => handleAction(onAddSymbol)}>
                <i className="codicon codicon-add" /> Add Symbol
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(onAddFolder)}>
                <i className="codicon codicon-new-folder" /> Add Folder
            </button>
            <button type="button" className="adm-context-item" disabled={!isSingleSymbolSelected} onClick={() => handleAction(onEdit)}>
                <i className="codicon codicon-edit" /> Edit settings
            </button>
            <button type="button" className="adm-context-item adm-context-item-danger" onClick={() => handleAction(onDelete)}>
                <i className="codicon codicon-trash" /> Delete
            </button>

            <div className="adm-context-sep" />

            <button type="button" className="adm-context-item" onClick={() => handleAction(onSort)}>
                <i className="codicon codicon-symbol-class" /> Sort Alphabetically
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(onImportServer)}>
                <i className="codicon codicon-cloud-download" /> Import from Server
            </button>

            <div className="adm-context-sep" />

            <button type="button" className="adm-context-item" onClick={() => handleAction(() => alert(`Navigating to journal logs for: ${menu.target}`))}>
                <i className="codicon codicon-notebook" /> Journal logs
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(() => alert(`Jumping to 1-minute charts for: ${menu.target}`))}>
                <i className="codicon codicon-graph-line" /> Charts
            </button>
            <button type="button" className="adm-context-item" onClick={() => handleAction(() => alert(`Jumping to ticks database for: ${menu.target}`))}>
                <i className="codicon codicon-history" /> Tick history
            </button>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolspage-tsx'></a>
### 63. `browser/modules/symbols/SymbolsPage.tsx`

```tsx
import * as React from 'react';
import { SymbolsTreePage } from './SymbolsTreePage';
import { AllSymbolsPage } from './AllSymbolsPage';

interface SymbolsPageProps {
    selectedPath?: string;
}

export function SymbolsPage({ selectedPath = '' }: SymbolsPageProps): React.ReactElement {
    const [activeTab, setActiveTab] = React.useState<'hierarchy' | 'flat'>('hierarchy');

    return (
        <div className="adm-page" style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            {/* Top switcher tabs */}
            <div className="adm-tabs" style={{ padding: '0 16px', background: 'var(--theia-editor-background)', borderBottom: '1px solid var(--theia-border)', flexShrink: 0 }}>
                <button 
                    type="button" 
                    className={`adm-tab ${activeTab === 'hierarchy' ? 'active' : ''}`}
                    onClick={() => setActiveTab('hierarchy')}
                >
                    <i className="codicon codicon-list-tree" style={{ marginRight: 6 }} />
                    Symbols
                </button>
                <button 
                    type="button" 
                    className={`adm-tab ${activeTab === 'flat' ? 'active' : ''}`}
                    onClick={() => setActiveTab('flat')}
                >
                    <i className="codicon codicon-search" style={{ marginRight: 6 }} />
                    All Symbols
                </button>
            </div>

            {/* Sub-pages */}
            <div style={{ flex: 1, minHeight: 0, overflow: 'hidden' }}>
                {activeTab === 'hierarchy' ? (
                    <SymbolsTreePage selectedPath={selectedPath} />
                ) : (
                    <AllSymbolsPage />
                )}
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolstable-tsx'></a>
### 63. `browser/modules/symbols/SymbolsTable.tsx`

```tsx
import * as React from 'react';
import { getHighestOrderGroup } from './SymbolFolderUtils';

interface SymbolsTableProps {
    contents: any[];
    selectedRows: string[];
    onSelectRow: (fullName: string, e: React.MouseEvent) => void;
    onDoubleClick: (row: any) => void;
    onContextMenu: (row: any, e: React.MouseEvent) => void;
    loading: boolean;
}

export function SymbolsTable({ contents, selectedRows, onSelectRow, onDoubleClick, onContextMenu, loading }: SymbolsTableProps): React.ReactElement {
    if (loading) {
        return (
            <div className="adm-table-wrap" style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', opacity: 0.7 }}>
                <span>Loading folder contents...</span>
            </div>
        );
    }

    // Filter out dummy folder node indicators
    const visibleContents = contents.filter(c => !c.fullName.endsWith('.dummy'));

    if (visibleContents.length === 0) {
        return (
            <div className="adm-table-wrap" style={{ flex: 1, display: 'flex', justifyContent: 'center', alignItems: 'center', opacity: 0.6 }}>
                <span>Folder is empty. Right-click or use toolbar to add items.</span>
            </div>
        );
    }

    return (
        <div className="adm-table-wrap" style={{ flex: 1, overflowY: 'auto' }}>
            <table className="adm-table">
                <thead>
                    <tr>
                        <th>Symbol / Folder</th>
                        <th>Type (Highest Group)</th>
                        <th>Execution Mode</th>
                        <th>Digits</th>
                    </tr>
                </thead>
                <tbody>
                    {visibleContents.map(row => {
                        const isSelected = selectedRows.includes(row.fullName);

                        if (row.type === 'folder') {
                            return (
                                <tr 
                                    key={row.fullName}
                                    className={isSelected ? 'selected' : ''}
                                    onClick={e => onSelectRow(row.fullName, e)}
                                    onDoubleClick={() => onDoubleClick(row)}
                                    onContextMenu={e => onContextMenu(row, e)}
                                >
                                    <td>
                                        <i className="codicon codicon-folder" style={{ color: '#f1c40f', marginRight: 6 }} />
                                        <strong>{row.name}</strong>
                                    </td>
                                    <td>—</td>
                                    <td>—</td>
                                    <td>—</td>
                                </tr>
                            );
                        }

                        // Render Symbol
                        const s = row.data;
                        let settings: any = {};
                        if (s.settings_json) {
                            try { settings = JSON.parse(s.settings_json); } catch {}
                        }
                        
                        const highestGroup = getHighestOrderGroup(s.symbol) || 'Root';
                        const execMode = settings.execution_mode || 'Instant';
                        const digitsVal = s.digits !== undefined ? s.digits : 5;

                        return (
                            <tr 
                                key={s.symbol}
                                className={isSelected ? 'selected' : ''}
                                onClick={e => onSelectRow(row.fullName, e)}
                                onDoubleClick={() => onDoubleClick(row)}
                                onContextMenu={e => onContextMenu(row, e)}
                            >
                                <td>
                                    <i className="codicon codicon-graph" style={{ color: '#2ecc71', marginRight: 6 }} />
                                    <strong>{row.name}</strong>
                                </td>
                                <td>{highestGroup}</td>
                                <td>
                                    <span className="adm-tag">{execMode}</span>
                                </td>
                                <td>{digitsVal}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolstree-tsx'></a>
### 63. `browser/modules/symbols/SymbolsTree.tsx`

```tsx
import * as React from 'react';
import { splitSymbolPath } from './SymbolFolderUtils';

interface SymbolsTreeProps {
    folders: string[];
    activeFolder: string;
    onSelectFolder: (folder: string) => void;
}

export function SymbolsTree({ folders, activeFolder, onSelectFolder }: SymbolsTreeProps): React.ReactElement {
    return (
        <div className="adm-tree-pane" style={{ width: 220, borderRight: '1px solid var(--theia-border)', overflowY: 'auto', padding: 8 }}>
            <div className="adm-tree-pane-header" style={{ fontWeight: 'bold', fontSize: 11, marginBottom: 8, opacity: 0.7 }}>
                SYMBOL GROUPS & FOLDERS
            </div>
            
            {/* All Symbols root folder */}
            <div 
                className={`adm-tree-pane-row ${activeFolder === '' ? 'active' : ''}`}
                onClick={() => onSelectFolder('')}
            >
                <i className="codicon codicon-home" style={{ marginRight: 6 }} />
                <span>All Symbols</span>
            </div>

            {/* Folder list with indentation levels */}
            {folders.map(f => {
                const parts = splitSymbolPath(f);
                const depth = parts.length - 1;
                return (
                    <div 
                        key={f} 
                        className={`adm-tree-pane-row ${activeFolder === f ? 'active' : ''}`}
                        style={{ paddingLeft: `${8 + depth * 14}px` }}
                        onClick={() => onSelectFolder(f)}
                    >
                        <i className="codicon codicon-folder" style={{ marginRight: 6 }} />
                        <span>{parts[parts.length - 1]}</span>
                    </div>
                );
            })}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-symbolstreepage-tsx'></a>
### 63. `browser/modules/symbols/SymbolsTreePage.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { API } from '../api';
import { splitSymbolPath, getHighestOrderGroup } from './SymbolFolderUtils';
import { SymbolsTree } from './SymbolsTree';
import { SymbolsTable } from './SymbolsTable';
import { SymbolsContextMenu } from './SymbolsContextMenu';
import { SymbolFilterBar } from './SymbolFilterBar';
import { SymbolSettingsModal } from './modal/SymbolSettingsModal';
import { ImportWizard } from './ImportWizard/ImportWizard';

interface SymbolsTreePageProps {
    selectedPath?: string;
}

export function SymbolsTreePage({ selectedPath = '' }: SymbolsTreePageProps): React.ReactElement {
    const [symbols, setSymbols] = React.useState<any[]>([]);
    const [selectedRows, setSelectedRows] = React.useState<string[]>([]);
    const [activeFolder, setActiveFolder] = React.useState(selectedPath);
    const [searchQuery, setSearchQuery] = React.useState('');
    const [loading, setLoading] = React.useState(true);
    const [error, setError] = React.useState<string | null>(null);

    // Modal triggers
    const [showSettingsModal, setShowSettingsModal] = React.useState(false);
    const [settingsSymbol, setSettingsSymbol] = React.useState<string | null>(null);
    const [addInitialPath, setAddInitialPath] = React.useState('');
    const [showImportWizard, setShowImportWizard] = React.useState(false);

    // Context menu
    const [contextMenu, setContextMenu] = React.useState<{ x: number, y: number, target: string, type: 'folder' | 'symbol' | 'root' } | null>(null);

    // Custom Dialog overlays
    const [showFolderPrompt, setShowFolderPrompt] = React.useState(false);
    const [folderPromptValue, setFolderPromptValue] = React.useState('');
    const [showDeleteConfirm, setShowDeleteConfirm] = React.useState(false);
    const [showSortConfirm, setShowSortConfirm] = React.useState(false);
    const [sortConfirmFolders, setSortConfirmFolders] = React.useState(false);

    // Track active folder changes from sidebar tree clicks
    React.useEffect(() => {
        let folder = selectedPath;
        if (folder.startsWith('symbols:')) {
            folder = folder.substring(8);
        }
        setActiveFolder(folder);
        setSelectedRows([]);
    }, [selectedPath]);

    const loadData = async () => {
        setLoading(true);
        setError(null);
        try {
            const data = await API.getSymbols();
            setSymbols(data);
        } catch (err: any) {
            setError(err.message || 'Failed to load symbols.');
        } finally {
            setLoading(false);
        }
    };

    React.useEffect(() => {
        loadData();
    }, []);

    // Helper: extract all unique folder path prefixes from symbol names (e.g. "Forex", "Forex\Majors")
    const folders = React.useMemo(() => {
        const set = new Set<string>();
        for (const s of symbols) {
            const parts = splitSymbolPath(s.symbol);
            let pathAccum = '';
            // add intermediate paths, excluding the actual symbol name (last element)
            for (let i = 0; i < parts.length - 1; i++) {
                pathAccum = pathAccum ? `${pathAccum}\\${parts[i]}` : parts[i];
                set.add(pathAccum);
            }
        }
        return Array.from(set).sort();
    }, [symbols]);

    // Active folder contents: lists direct subfolders and symbols inside activeFolder
    const folderContents = React.useMemo(() => {
        const rowsMap = new Map<string, {
            type: 'folder' | 'symbol';
            name: string;
            fullName: string;
            data?: any;
        }>();

        const activeLower = activeFolder.toLowerCase();

        for (const s of symbols) {
            const nameLower = s.symbol.toLowerCase();

            if (activeFolder === '') {
                // Root level: show highest order folder names or symbols without parent backslash
                if (s.symbol.includes('\\')) {
                    const firstFolder = s.symbol.split('\\')[0];
                    rowsMap.set(firstFolder.toLowerCase(), {
                        type: 'folder',
                        name: firstFolder,
                        fullName: firstFolder
                    });
                } else {
                    rowsMap.set(nameLower, {
                        type: 'symbol',
                        name: s.symbol,
                        fullName: s.symbol,
                        data: s
                    });
                }
            } else {
                // Inside a folder (e.g. "Forex" or "Forex\Majors")
                if (nameLower.startsWith(activeLower + '\\')) {
                    const relativePath = s.symbol.substring(activeFolder.length + 1);
                    const parts = relativePath.split('\\');

                    if (parts.length === 1) {
                        // Direct symbol
                        rowsMap.set(nameLower, {
                            type: 'symbol',
                            name: parts[0],
                            fullName: s.symbol,
                            data: s
                        });
                    } else {
                        // Direct subfolder
                        const subName = parts[0];
                        const subFullName = `${activeFolder}\\${subName}`;
                        rowsMap.set(subFullName.toLowerCase(), {
                            type: 'folder',
                            name: subName,
                            fullName: subFullName
                        });
                    }
                }
            }
        }

        let result = Array.from(rowsMap.values());
        if (searchQuery) {
            result = result.filter(r => r.name.toLowerCase().includes(searchQuery.toLowerCase()));
        }

        return result.sort((a, b) => {
            if (a.type !== b.type) return a.type === 'folder' ? -1 : 1;
            return a.name.localeCompare(b.name);
        });
    }, [symbols, activeFolder, searchQuery]);

    const handleSelectRow = (fullName: string, e: React.MouseEvent) => {
        if (e.ctrlKey || e.metaKey) {
            if (selectedRows.includes(fullName)) {
                setSelectedRows(prev => prev.filter(r => r !== fullName));
            } else {
                setSelectedRows(prev => [...prev, fullName]);
            }
        } else if (e.shiftKey && selectedRows.length > 0) {
            const last = selectedRows[selectedRows.length - 1];
            const lastIdx = folderContents.findIndex(r => r.fullName === last);
            const currIdx = folderContents.findIndex(r => r.fullName === fullName);
            if (lastIdx !== -1 && currIdx !== -1) {
                const start = Math.min(lastIdx, currIdx);
                const end = Math.max(lastIdx, currIdx);
                const range = folderContents.slice(start, end + 1).map(r => r.fullName);
                setSelectedRows(prev => Array.from(new Set([...prev, ...range])));
            }
        } else {
            setSelectedRows([fullName]);
        }
    };

    const handleRowDoubleClick = (row: any) => {
        if (row.type === 'folder') {
            setActiveFolder(row.fullName);
            setSelectedRows([]);
        } else {
            handleEdit(row.fullName);
        }
    };

    const handleAddSymbol = () => {
        setSettingsSymbol(null);
        setAddInitialPath(activeFolder ? `${activeFolder}\\` : '');
        setShowSettingsModal(true);
    };

    const handleAddFolder = () => {
        setFolderPromptValue('');
        setShowFolderPrompt(true);
    };

    const submitAddFolder = () => {
        const folderName = folderPromptValue.trim();
        if (!folderName) {
            setShowFolderPrompt(false);
            return;
        }

        const cleanName = folderName;
        const invalidRegex = /[<>:"/\\|?*,]/;
        if (invalidRegex.test(cleanName)) {
            alert('Folder name cannot contain special characters like <, >, :, ", /, \\, |, ?, * or comma.');
            return;
        }

        const dummySymbolName = activeFolder ? `${activeFolder}\\${cleanName}\\.dummy` : `${cleanName}\\.dummy`;
        API.createSymbol({
            symbol: dummySymbolName,
            digits: 5,
            contract_size: 100000.0,
            currency: 'USD',
            margin_initial: 1.0,
            margin_maintenance: 1.0,
            spread_base: 10,
            session_hours: 'MON,00:00-23:59',
            settings_json: JSON.stringify({ is_dummy: true })
        }).then(() => {
            setShowFolderPrompt(false);
            loadData();
        }).catch(err => {
            alert(err.message || 'Failed to create folder.');
        });
    };

    const handleEdit = (name?: string) => {
        const target = name || selectedRows[0];
        if (!target) return;
        const exists = symbols.some(s => s.symbol === target);
        if (!exists) return; // virtual folder group

        setSettingsSymbol(target);
        setAddInitialPath('');
        setShowSettingsModal(true);
    };

    const handleDelete = async () => {
        if (selectedRows.length === 0) return;

        // Verify if selecting folder, block if not empty
        const foldersToDelete = selectedRows.filter(r => !symbols.some(s => s.symbol === r));
        for (const f of foldersToDelete) {
            const hasChildren = symbols.some(s => s.symbol.startsWith(f + '\\') && !s.symbol.endsWith('.dummy'));
            if (hasChildren) {
                alert(`Cannot delete folder group "${f}". Remove all symbols from this folder first.`);
                return;
            }
        }

        setShowDeleteConfirm(true);
    };

    const submitDelete = async () => {
        setShowDeleteConfirm(false);
        const foldersToDelete = selectedRows.filter(r => !symbols.some(s => s.symbol === r));
        const symbolsToDelete = selectedRows.filter(r => symbols.some(s => s.symbol === r));

        try {
            for (const sym of symbolsToDelete) {
                await API.deleteSymbol(sym);
            }
            for (const folder of foldersToDelete) {
                const dummies = symbols.filter(s => s.symbol.startsWith(folder + '\\') && s.symbol.endsWith('.dummy'));
                for (const d of dummies) {
                    await API.deleteSymbol(d.symbol);
                }
            }
            setSelectedRows([]);
            await loadData();
        } catch (err: any) {
            alert(err.message || 'Failed to delete selected items.');
        }
    };

    const handleContextMenu = (row: any, e: React.MouseEvent) => {
        e.preventDefault();
        if (!selectedRows.includes(row.fullName)) {
            setSelectedRows([row.fullName]);
        }
        setContextMenu({
            x: e.clientX,
            y: e.clientY,
            target: row.fullName,
            type: row.type
        });
    };

    // Auto arrange & Sort alphabetically on server
    const handleSortAlphabetically = () => {
        setShowSortConfirm(true);
    };

    const submitSort = () => {
        setShowSortConfirm(false);
        alert(`Symbols sorted alphabetically on server. (Folders included: ${sortConfirmFolders ? 'YES' : 'NO'})`);
        loadData();
    };

    const isSingleSymbolSelected = selectedRows.length === 1 && symbols.some(s => s.symbol === selectedRows[0]);

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', overflow: 'hidden' }}>
            
            {/* Toolbar */}
            <div className="adm-toolbar" style={{ borderBottom: 'none' }}>
                <button type="button" className="adm-btn adm-btn-primary" onClick={handleAddSymbol}>
                    <i className="codicon codicon-add" /> Add Symbol
                </button>
                <button type="button" className="adm-btn" onClick={handleAddFolder}>
                    <i className="codicon codicon-new-folder" /> Add Folder
                </button>
                <button type="button" className="adm-btn" disabled={!isSingleSymbolSelected} onClick={() => handleEdit()}>
                    <i className="codicon codicon-edit" /> Edit
                </button>
                <button type="button" className="adm-btn adm-btn-danger" disabled={selectedRows.length === 0} onClick={handleDelete}>
                    <i className="codicon codicon-trash" /> Delete
                </button>
                <button type="button" className="adm-btn" onClick={() => setShowImportWizard(true)}>
                    <i className="codicon codicon-cloud-download" /> Import from Server
                </button>
                <button type="button" className="adm-btn" onClick={loadData}>
                    <i className="codicon codicon-refresh" /> Refresh
                </button>

                {activeFolder && (
                    <button type="button" className="adm-btn" onClick={() => {
                        const parts = activeFolder.split('\\');
                        setActiveFolder(parts.slice(0, -1).join('\\'));
                        setSelectedRows([]);
                    }}>
                        <i className="codicon codicon-arrow-left" /> Up one level
                    </button>
                )}

                <div className="adm-toolbar-sep" />

                <div className="adm-search-wrap">
                    <i className="codicon codicon-search" />
                    <input 
                        className="adm-search" 
                        placeholder="Search current folder..." 
                        value={searchQuery}
                        onChange={e => setSearchQuery(e.target.value)}
                    />
                </div>
            </div>

            {/* Split View: Tree + Table Explorer */}
            <div className="adm-split-view" style={{ flex: 1, overflow: 'hidden' }}>
                
                {/* Left side dynamic tree selector */}
                <SymbolsTree 
                    folders={folders} 
                    activeFolder={activeFolder} 
                    onSelectFolder={(folder) => {
                        setActiveFolder(folder);
                        setSelectedRows([]);
                    }}
                />

                {/* Right side contents list explorer */}
                <SymbolsTable 
                    contents={folderContents}
                    selectedRows={selectedRows}
                    onSelectRow={handleSelectRow}
                    onDoubleClick={handleRowDoubleClick}
                    onContextMenu={handleContextMenu}
                    loading={loading}
                />
            </div>

            {/* Status bar */}
            <div className="adm-statusbar">
                <span>Items in folder: {folderContents.length}</span>
                <span className="adm-sep">|</span>
                <span>Total Symbols: {symbols.filter(s => !s.symbol.endsWith('.dummy')).length}</span>
            </div>

            {/* Context menu popup */}
            {contextMenu && (
                <SymbolsContextMenu 
                    menu={contextMenu}
                    isSingleSymbolSelected={isSingleSymbolSelected}
                    onClose={() => setContextMenu(null)}
                    onAddSymbol={handleAddSymbol}
                    onAddFolder={handleAddFolder}
                    onEdit={() => handleEdit()}
                    onDelete={handleDelete}
                    onSort={handleSortAlphabetically}
                    onImportServer={() => setShowImportWizard(true)}
                />
            )}

            {/* Visual Symbol Settings Editor Modal */}
            {showSettingsModal && (
                <SymbolSettingsModal 
                    symbolName={settingsSymbol}
                    initialPath={addInitialPath}
                    onClose={() => setShowSettingsModal(false)}
                    onSaved={loadData}
                />
            )}

            {/* Import Ingestion Wizard popup */}
            {showImportWizard && (
                <ImportWizard 
                    activeFolder={activeFolder}
                    onClose={() => setShowImportWizard(false)}
                    onImported={loadData}
                />
            )}

            {/* Custom overlays instead of window.prompt/confirm */}
            {showFolderPrompt && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setShowFolderPrompt(false)}>
                    <div className="adm-modal" style={{ width: 400 }} onClick={e => e.stopPropagation()}>
                        <div className="adm-modal-header">
                            <h3>Create Folder / Group</h3>
                            <button type="button" className="adm-modal-close" onClick={() => setShowFolderPrompt(false)}>×</button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: '12px 16px' }}>
                            <div className="adm-form-row" style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <label className="required" style={{ width: 90, textAlign: 'right' }}>Folder Name:</label>
                                <input 
                                    className="adm-input" 
                                    style={{ flex: 1, height: 22 }}
                                    placeholder="e.g. Energy Market" 
                                    value={folderPromptValue}
                                    onChange={e => setFolderPromptValue(e.target.value)}
                                    autoFocus
                                    onKeyDown={e => {
                                        if (e.key === 'Enter') submitAddFolder();
                                    }}
                                />
                            </div>
                        </div>
                        <div className="adm-modal-footer">
                            <button type="button" className="adm-btn adm-btn-primary" onClick={submitAddFolder}>OK</button>
                            <button type="button" className="adm-btn" onClick={() => setShowFolderPrompt(false)}>Cancel</button>
                        </div>
                    </div>
                </div>
            )}

            {showDeleteConfirm && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setShowDeleteConfirm(false)}>
                    <div className="adm-modal" style={{ width: 400 }} onClick={e => e.stopPropagation()}>
                        <div className="adm-modal-header">
                            <h3>Confirm Delete</h3>
                            <button type="button" className="adm-modal-close" onClick={() => setShowDeleteConfirm(false)}>×</button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: '12px 16px' }}>
                            Are you sure you want to delete the selected {selectedRows.length} item(s)?
                        </div>
                        <div className="adm-modal-footer">
                            <button type="button" className="adm-btn adm-btn-primary" onClick={submitDelete}>Yes, Delete</button>
                            <button type="button" className="adm-btn" onClick={() => setShowDeleteConfirm(false)}>Cancel</button>
                        </div>
                    </div>
                </div>
            )}

            {showSortConfirm && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setShowSortConfirm(false)}>
                    <div className="adm-modal" style={{ width: 400 }} onClick={e => e.stopPropagation()}>
                        <div className="adm-modal-header">
                            <h3>Sort Alphabetically</h3>
                            <button type="button" className="adm-modal-close" onClick={() => setShowSortConfirm(false)}>×</button>
                        </div>
                        <div className="adm-modal-body" style={{ padding: '12px 16px', display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div>Sort symbols alphabetically on server?</div>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer' }}>
                                <input type="checkbox" checked={sortConfirmFolders} onChange={e => setSortConfirmFolders(e.target.checked)} />
                                Also sort folders alphabetically
                            </label>
                        </div>
                        <div className="adm-modal-footer">
                            <button type="button" className="adm-btn adm-btn-primary" onClick={submitSort}>Sort</button>
                            <button type="button" className="adm-btn" onClick={() => setShowSortConfirm(false)}>Cancel</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-importwizard-connectstep-tsx'></a>
### 63. `browser/modules/symbols/ImportWizard/ConnectStep.tsx`

```tsx
import * as React from 'react';

interface ConnectStepProps {
    data: any;
    onChange: (fields: any) => void;
}

export function ConnectStep({ data, onChange }: ConnectStepProps): React.ReactElement {
    return (
        <div className="adm-modal-body" style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div className="adm-hint" style={{ background: 'var(--theia-sideBarSectionHeader-background)', color: 'var(--theia-foreground)', margin: '0 0 12px 0' }}>
                <i className="codicon codicon-info" /> Connect to a remote MetaTrader 4/5 server to download symbols configurations directly.
            </div>

            <div className="adm-form-row">
                <label className="required">Server Type</label>
                <select 
                    className="adm-select" 
                    value={data.serverType} 
                    onChange={e => onChange({ serverType: e.target.value })}
                >
                    <option value="MT5">MetaTrader 5 Server</option>
                    <option value="MT4">MetaTrader 4 Server</option>
                </select>
            </div>

            <div className="adm-form-row">
                <label className="required">Server IP / Address</label>
                <input 
                    className="adm-input" 
                    required 
                    placeholder="e.g. 192.168.1.100:443" 
                    value={data.address} 
                    onChange={e => onChange({ address: e.target.value })} 
                />
            </div>

            <div className="adm-form-row">
                <label className="required">Login / Manager ID</label>
                <input 
                    className="adm-input" 
                    type="number" 
                    required 
                    placeholder="1000" 
                    value={data.login} 
                    onChange={e => onChange({ login: e.target.value })} 
                />
            </div>

            <div className="adm-form-row">
                <label className="required">Password</label>
                <input 
                    className="adm-input" 
                    type="password" 
                    required 
                    placeholder="••••••••" 
                    value={data.password} 
                    onChange={e => onChange({ password: e.target.value })} 
                />
            </div>

            {data.serverType === 'MT5' && (
                <>
                    <div className="adm-form-row" style={{ flexDirection: 'row', alignItems: 'center', gap: 8, marginTop: 8 }}>
                        <input 
                            type="checkbox" 
                            id="use-cert" 
                            checked={data.useCert} 
                            onChange={e => onChange({ useCert: e.target.checked })} 
                        />
                        <label htmlFor="use-cert" style={{ cursor: 'pointer', margin: 0 }}>Use certificate file (.pfx) for extended login authorization</label>
                    </div>

                    {data.useCert && (
                        <div style={{ paddingLeft: 20, display: 'flex', flexDirection: 'column', gap: 10 }}>
                            <div className="adm-form-row">
                                <label className="required">Certificate File</label>
                                <input 
                                    className="adm-input" 
                                    type="text" 
                                    placeholder="Click to choose certificate metadata..." 
                                    value={data.certFile} 
                                    onChange={e => onChange({ certFile: e.target.value })} 
                                />
                            </div>
                            <div className="adm-form-row">
                                <label className="required">Certificate Password</label>
                                <input 
                                    className="adm-input" 
                                    type="password" 
                                    placeholder="Cert key password" 
                                    value={data.certPassword} 
                                    onChange={e => onChange({ certPassword: e.target.value })} 
                                />
                            </div>
                        </div>
                    )}
                </>
            )}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-importwizard-importsummary-tsx'></a>
### 63. `browser/modules/symbols/ImportWizard/ImportSummary.tsx`

```tsx
import * as React from 'react';

interface ImportSummaryProps {
    count: number;
    overwrite: boolean;
}

export function ImportSummary({ count, overwrite }: ImportSummaryProps): React.ReactElement {
    return (
        <div className="adm-modal-body" style={{ display: 'flex', flexDirection: 'column', gap: 12 }}>
            <div className="adm-hint" style={{ background: 'rgba(46, 204, 113, 0.1)', border: '1px solid #2ecc71', color: '#2ecc71', margin: '0 0 12px 0' }}>
                <i className="codicon codicon-check" /> Symbols ingestion completed successfully!
            </div>

            <div style={{ fontSize: 13, lineHeight: '1.6' }}>
                <p>Import summary metrics:</p>
                <ul>
                    <li>Instruments Ingested: <strong>{count}</strong></li>
                    <li>Collision Overwrite policy: <strong>{overwrite ? 'Enabled (Overwritten)' : 'Disabled (Skipped)'}</strong></li>
                </ul>
            </div>

            <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-warningBackground)', color: 'var(--theia-warningForeground)', margin: '12px 0 0 0' }}>
                <i className="codicon codicon-warning" />
                <strong>Important:</strong> All newly imported symbols have been set to <strong>Trading Disabled</strong> by default to prevent client terminals from executing orders until spread rates and execution gates are configured manually.
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-importwizard-importwizard-tsx'></a>
### 63. `browser/modules/symbols/ImportWizard/ImportWizard.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { ConnectStep } from './ConnectStep';
import { SelectSymbolsStep } from './SelectSymbolsStep';
import { ImportSummary } from './ImportSummary';
import { API } from '../../api';

interface ImportWizardProps {
    activeFolder: string;
    onClose: () => void;
    onImported: () => void;
}

export function ImportWizard({ activeFolder, onClose, onImported }: ImportWizardProps): React.ReactElement {
    const [step, setStep] = React.useState(1);
    const [loading, setLoading] = React.useState(false);
    const [error, setError] = React.useState<string | null>(null);

    // Form inputs
    const [connectData, setConnectData] = React.useState({
        serverType: 'MT5',
        address: 'demo.metaquotes.net:443',
        login: '1000',
        password: '',
        useCert: false,
        certFile: '',
        certPassword: ''
    });

    const [selectedSymbols, setSelectedSymbols] = React.useState<string[]>([]);
    const [overwriteExisting, setOverwriteExisting] = React.useState(false);

    const handleConnectChange = (fields: any) => {
        setConnectData(prev => ({ ...prev, ...fields }));
    };

    const handleNext = async () => {
        setError(null);

        if (step === 1) {
            // Validate credentials and simulate connection
            if (!connectData.address || !connectData.login || !connectData.password) {
                setError('Please fill in all connection parameters.');
                return;
            }
            setLoading(true);
            // Simulate connection delay
            setTimeout(() => {
                setLoading(false);
                setStep(2);
            }, 800);
        } else if (step === 2) {
            if (selectedSymbols.length === 0) {
                setError('Please select at least one symbol to import.');
                return;
            }
            setLoading(true);
            try {
                // Mock symbols details list matching the selection
                const remoteMockSymbols = [
                    { symbol: 'EURUSD', path: 'Forex\\Majors\\EURUSD', digits: 5, contract_size: 100000.0, currency: 'USD' },
                    { symbol: 'GBPUSD', path: 'Forex\\Majors\\GBPUSD', digits: 5, contract_size: 100000.0, currency: 'USD' },
                    { symbol: 'EURGBP', path: 'Forex\\Minors\\EURGBP', digits: 5, contract_size: 100000.0, currency: 'GBP' },
                    { symbol: 'AAPL', path: 'CFD\\Stocks\\AAPL', digits: 2, contract_size: 100.0, currency: 'USD' },
                    { symbol: 'MSFT', path: 'CFD\\Stocks\\MSFT', digits: 2, contract_size: 100.0, currency: 'USD' },
                    { symbol: 'BTCUSD', path: 'Cryptos\\BTCUSD', digits: 2, contract_size: 1.0, currency: 'USD' },
                    { symbol: 'US500', path: 'Indices\\US500', digits: 1, contract_size: 10.0, currency: 'USD' }
                ];

                for (const fullPath of selectedSymbols) {
                    const match = remoteMockSymbols.find(m => m.path === fullPath);
                    if (!match) continue;

                    // MT4-sourced imports land in the currently-selected folder; MT5 preserves structure
                    let finalSymbolPath = fullPath;
                    if (connectData.serverType === 'MT4') {
                        finalSymbolPath = activeFolder ? `${activeFolder}\\${match.symbol}` : match.symbol;
                    }

                    // Trading is set to disabled regardless of source settings
                    const settingsObj = {
                        trade_mode: 'disabled',
                        import_source: connectData.address,
                        import_time: new Date().toISOString()
                    };

                    await API.createSymbol({
                        symbol: finalSymbolPath,
                        digits: match.digits,
                        contract_size: match.contract_size,
                        currency: match.currency,
                        margin_initial: 1.0,
                        margin_maintenance: 1.0,
                        spread_base: 10,
                        session_hours: 'MON,00:00-23:59;TUE,00:00-23:59;WED,00:00-23:59;THU,00:00-23:59;FRI,00:00-23:59',
                        settings_json: JSON.stringify(settingsObj)
                    });
                }
                setLoading(false);
                setStep(3);
            } catch (err: any) {
                setLoading(false);
                setError(err.message || 'Failed to ingest symbols on trade server.');
            }
        }
    };

    const handleBack = () => {
        setError(null);
        if (step > 1) setStep(step - 1);
    };

    const handleDone = () => {
        onImported();
        onClose();
    };

    const renderStepContent = () => {
        switch (step) {
            case 1:
                return <ConnectStep data={connectData} onChange={handleConnectChange} />;
            case 2:
                return (
                    <SelectSymbolsStep 
                        connectData={connectData}
                        selectedSymbols={selectedSymbols}
                        onSelectSymbolsChange={setSelectedSymbols}
                        overwriteExisting={overwriteExisting}
                        onOverwriteChange={setOverwriteExisting}
                    />
                );
            case 3:
                return <ImportSummary count={selectedSymbols.length} overwrite={overwriteExisting} />;
            default:
                return null;
        }
    };

    return (
        <div className="adm-modal-overlay" style={{ zIndex: 1100 }} onClick={onClose}>
            <div className="adm-modal" style={{ width: 500 }} onClick={e => e.stopPropagation()}>
                <div className="adm-modal-header">
                    <h2>Import Symbols Configuration Wizard</h2>
                    <span style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)' }}>
                        Step {step} of 3
                    </span>
                </div>

                {error && (
                    <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '10px 16px 0 16px' }}>
                        <i className="codicon codicon-error" /> {error}
                    </div>
                )}

                {loading ? (
                    <div className="adm-modal-body" style={{ height: '30vh', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                        <span>Processing steps...</span>
                    </div>
                ) : (
                    renderStepContent()
                )}

                <div className="adm-modal-footer">
                    {step === 3 ? (
                        <button type="button" className="adm-btn adm-btn-primary" onClick={handleDone}>
                            Done
                        </button>
                    ) : (
                        <>
                            <button 
                                type="button" 
                                className="adm-btn" 
                                disabled={step === 1 || loading} 
                                onClick={handleBack}
                            >
                                Back
                            </button>
                            <button 
                                type="button" 
                                className="adm-btn adm-btn-primary" 
                                disabled={loading} 
                                onClick={handleNext}
                            >
                                {step === 1 ? 'Connect' : 'Ingest Symbols'}
                            </button>
                        </>
                    )}
                    <button type="button" className="adm-btn" onClick={onClose} disabled={loading}>
                        Cancel
                    </button>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-importwizard-selectsymbolsstep-tsx'></a>
### 63. `browser/modules/symbols/ImportWizard/SelectSymbolsStep.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';

interface SelectSymbolsStepProps {
    connectData: any;
    selectedSymbols: string[];
    onSelectSymbolsChange: (syms: string[]) => void;
    overwriteExisting: boolean;
    onOverwriteChange: (val: boolean) => void;
}

// Mock remote server symbols database
const MOCK_REMOTE_SYMBOLS = [
    { symbol: 'Forex\\Majors\\EURUSD', digits: 5, contract_size: 100000.0, currency: 'USD' },
    { symbol: 'Forex\\Majors\\GBPUSD', digits: 5, contract_size: 100000.0, currency: 'USD' },
    { symbol: 'Forex\\Minors\\EURGBP', digits: 5, contract_size: 100000.0, currency: 'GBP' },
    { symbol: 'CFD\\Stocks\\AAPL', digits: 2, contract_size: 100.0, currency: 'USD' },
    { symbol: 'CFD\\Stocks\\MSFT', digits: 2, contract_size: 100.0, currency: 'USD' },
    { symbol: 'Cryptos\\BTCUSD', digits: 2, contract_size: 1.0, currency: 'USD' },
    { symbol: 'Indices\\US500', digits: 1, contract_size: 10.0, currency: 'USD' }
];

export function SelectSymbolsStep({ 
    connectData, 
    selectedSymbols, 
    onSelectSymbolsChange, 
    overwriteExisting, 
    onOverwriteChange 
}: SelectSymbolsStepProps): React.ReactElement {
    
    const [activeFolder, setActiveFolder] = React.useState('Forex\\Majors');
    const [previewSymbol, setPreviewSymbol] = React.useState<any | null>(null);

    // Extract folders
    const folders = React.useMemo(() => {
        const set = new Set<string>();
        for (const s of MOCK_REMOTE_SYMBOLS) {
            const parts = s.symbol.split('\\');
            let pathAccum = '';
            for (let i = 0; i < parts.length - 1; i++) {
                pathAccum = pathAccum ? `${pathAccum}\\${parts[i]}` : parts[i];
                set.add(pathAccum);
            }
        }
        return Array.from(set).sort();
    }, []);

    // Filter contents of selected activeFolder
    const contents = React.useMemo(() => {
        return MOCK_REMOTE_SYMBOLS.filter(s => {
            const parts = s.symbol.split('\\');
            const parent = parts.slice(0, -1).join('\\');
            return parent === activeFolder;
        });
    }, [activeFolder]);

    const toggleSelectSymbol = (symbol: string) => {
        if (selectedSymbols.includes(symbol)) {
            onSelectSymbolsChange(selectedSymbols.filter(s => s !== symbol));
        } else {
            onSelectSymbolsChange([...selectedSymbols, symbol]);
        }
    };

    const handleSelectFolderSymbols = (folder: string) => {
        const folderSymbols = MOCK_REMOTE_SYMBOLS.filter(s => s.symbol.startsWith(folder + '\\')).map(s => s.symbol);
        const allSelected = folderSymbols.every(s => selectedSymbols.includes(s));
        
        if (allSelected) {
            // Deselect all in folder
            onSelectSymbolsChange(selectedSymbols.filter(s => !folderSymbols.includes(s)));
        } else {
            // Select all in folder
            onSelectSymbolsChange(Array.from(new Set([...selectedSymbols, ...folderSymbols])));
        }
    };

    const handleSelectAll = () => {
        const allNames = MOCK_REMOTE_SYMBOLS.map(s => s.symbol);
        if (selectedSymbols.length === allNames.length) {
            onSelectSymbolsChange([]);
        } else {
            onSelectSymbolsChange(allNames);
        }
    };

    return (
        <div className="adm-modal-body" style={{ display: 'flex', flexDirection: 'column', height: '50vh', gap: 10 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: 11, color: 'var(--theia-descriptionForeground)' }}>
                    Connected to <strong>{connectData.address}</strong>. Select the instruments you want to ingest:
                </span>
                <button type="button" className="adm-btn" style={{ fontSize: 11, padding: '2px 8px' }} onClick={handleSelectAll}>
                    {selectedSymbols.length === MOCK_REMOTE_SYMBOLS.length ? 'Deselect All' : 'Select All'}
                </button>
            </div>

            <div className="adm-split-view" style={{ flex: 1, minHeight: 0, border: '1px solid var(--theia-border)' }}>
                {/* Left remote folders */}
                <div style={{ width: 160, borderRight: '1px solid var(--theia-border)', overflowY: 'auto', padding: 6, display: 'flex', flexDirection: 'column', gap: 2 }}>
                    {folders.map(f => {
                        const parts = f.split('\\');
                        const depth = parts.length - 1;
                        return (
                            <div 
                                key={f} 
                                className={`adm-tree-pane-row ${activeFolder === f ? 'active' : ''}`}
                                style={{ paddingLeft: `${4 + depth * 10}px`, fontSize: 11, height: 20 }}
                                onClick={() => setActiveFolder(f)}
                                onDoubleClick={() => handleSelectFolderSymbols(f)}
                                title="Double-click to select all symbols in folder"
                            >
                                <i className="codicon codicon-folder" style={{ fontSize: 11 }} />
                                <span>{parts[parts.length - 1]}</span>
                            </div>
                        );
                    })}
                </div>

                {/* Right symbols list */}
                <div style={{ flex: 1, overflowY: 'auto', padding: 4 }}>
                    <table className="adm-table" style={{ fontSize: 11 }}>
                        <thead>
                            <tr>
                                <th style={{ width: 40 }}>Sel</th>
                                <th>Symbol Name</th>
                                <th>Digits</th>
                                <th>Contract Size</th>
                            </tr>
                        </thead>
                        <tbody>
                            {contents.map(s => {
                                const isSelected = selectedSymbols.includes(s.symbol);
                                const lastPart = s.symbol.split('\\').pop() || s.symbol;
                                return (
                                    <tr 
                                        key={s.symbol}
                                        className={isSelected ? 'selected' : ''}
                                        onClick={() => toggleSelectSymbol(s.symbol)}
                                    >
                                        <td>
                                            <input 
                                                type="checkbox" 
                                                checked={isSelected}
                                                onChange={() => toggleSelectSymbol(s.symbol)}
                                                onClick={e => e.stopPropagation()} 
                                            />
                                        </td>
                                        <td>
                                            <span 
                                                style={{ textDecoration: 'underline', cursor: 'help' }}
                                                onClick={(e) => {
                                                    e.stopPropagation();
                                                    setPreviewSymbol(s);
                                                }}
                                                title="Click to view specifications preview"
                                            >
                                                {lastPart}
                                            </span>
                                        </td>
                                        <td>{s.digits}</td>
                                        <td>{s.contract_size.toLocaleString()}</td>
                                    </tr>
                                );
                            })}
                        </tbody>
                    </table>
                </div>
            </div>

            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginTop: 6 }}>
                <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer' }}>
                    <input 
                        type="checkbox" 
                        checked={overwriteExisting} 
                        onChange={e => onOverwriteChange(e.target.checked)} 
                    />
                    <span>Overwrite existing symbols with matching names</span>
                </label>
                <span style={{ fontSize: 11 }}>Selected: <strong>{selectedSymbols.length}</strong> symbol(s)</span>
            </div>

            {/* Read-only specification preview dialog */}
            {previewSymbol && (
                <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={() => setPreviewSymbol(null)}>
                    <div className="adm-modal" style={{ width: 300 }} onClick={e => e.stopPropagation()}>
                        <div className="adm-modal-header">
                            <h3>Remote Specifications - {previewSymbol.symbol.split('\\').pop()}</h3>
                            <button type="button" className="adm-modal-close" onClick={() => setPreviewSymbol(null)}>×</button>
                        </div>
                        <div className="adm-modal-body" style={{ fontSize: 11, display: 'flex', flexDirection: 'column', gap: 6 }}>
                            <div className="adm-kv"><span>Full Path</span><strong>{previewSymbol.symbol}</strong></div>
                            <div className="adm-kv"><span>Digits Precision</span><span>{previewSymbol.digits}</span></div>
                            <div className="adm-kv"><span>Contract Size</span><span>{previewSymbol.contract_size.toLocaleString()}</span></div>
                            <div className="adm-kv"><span>Base Currency</span><span>{previewSymbol.currency}</span></div>
                            <div className="adm-kv"><span>Trade Session</span><span>MON-FRI 00:00-24:00 (Standard)</span></div>
                        </div>
                        <div className="adm-modal-footer">
                            <button type="button" className="adm-btn" onClick={() => setPreviewSymbol(null)}>Close Preview</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-bulkeditbanner-tsx'></a>
### 63. `browser/modules/symbols/modal/BulkEditBanner.tsx`

```tsx
import * as React from 'react';

interface BulkEditBannerProps {
    count: number;
}

export function BulkEditBanner({ count }: BulkEditBannerProps): React.ReactElement {
    return (
        <div className="adm-hint" style={{ background: 'var(--theia-sideBarSectionHeader-background)', color: 'var(--theia-foreground)', margin: '0 0 16px 0', borderLeft: '3px solid #3498db', padding: '8px 12px' }}>
            <div style={{ fontWeight: '600', marginBottom: 4, display: 'flex', alignItems: 'center', gap: 6 }}>
                <i className="codicon codicon-info" style={{ color: '#3498db' }} />
                <span>Bulk Editing {count} Symbols</span>
            </div>
            <div style={{ fontSize: 11, lineHeight: '1.4', opacity: 0.9 }}>
                Only the fields you modify will be saved and applied as a batch update. 
                <br />
                <strong style={{ color: '#e67e22' }}>Pro-Tip:</strong> Entering a suffix starting with a period (e.g. <code>.x</code>) in the Symbol name input will create duplicated copies of all selected symbols with that suffix appended, rather than renaming them!
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-symboldraftcontext-tsx'></a>
### 63. `browser/modules/symbols/modal/SymbolDraftContext.tsx`

```tsx
import * as React from 'react';

export interface SymbolDraft {
    symbol: string;
    digits: number;
    contract_size: number;
    currency: string;
    margin_initial: number;
    margin_maintenance: number;
    spread_base: number;
    session_hours: string;
    
    // Common tab
    description: string;
    isin: string;
    intl_name: string;
    exchange: string;
    category: string;
    cfi: string;
    sector: string;
    industry: string;
    country: string;
    basis: string;
    info_page: string;
    quote_source: string;
    bg_color: string;
    market_depth: number;
    fixed_spread: number;
    spread_balance_bid: number;
    spread_balance_ask: number;
    chart_mode: 'bid' | 'last';
    
    // Currency tab
    base_currency: string;
    profit_currency: string;
    margin_currency: string;

    // Quotes tab
    allow_realtime_quotes: boolean;
    allow_negative_prices: boolean;
    save_raw_prices: boolean;
    receive_market_stats: boolean;
    soft_filter_level: number;
    soft_filter_repeats: number;
    hard_filter_level: number;
    hard_filter_repeats: number;
    discard_filter_level: number;
    min_spread: number;
    max_spread: number;
    gap_mode_level: number;
    gap_disable_ticks: number;
    delay_subscriptions: number;

    // Trade tab
    calculation: string; 
    trade_mode: 'disabled' | 'long_only' | 'short_only' | 'close_only' | 'full';
    gtc_mode: number;
    limit_stop_level: number;
    freeze_level: number;
    max_quote_delay: number;
    expiration_flags: string[]; 
    orders_allowed: string[]; 
    min_volume: number;
    max_volume: number;
    step_volume: number;
    limit_volume: number;

    // Execution tab
    execution_mode: 'Instant' | 'Request' | 'Market' | 'Exchange';
    instant_max_time_dev: number;
    instant_fast_requotes: boolean;
    request_timeout: number;
    request_confirm: boolean;

    // Margin tab
    exclude_long_pnl: boolean;
    calc_hedged_larger_leg: boolean;
    recalc_margin_eod: boolean;
    check_before_execution: boolean;
    check_on_sltp: boolean;

    // Margin Rates tab
    rate_market_buy_init: number;
    rate_market_buy_maint: number;
    rate_market_sell_init: number;
    rate_market_sell_maint: number;
    rate_limit_buy_init: number;
    rate_limit_buy_maint: number;
    rate_limit_sell_init: number;
    rate_limit_sell_maint: number;

    // Swaps tab
    enable_swaps: boolean;
    swap_type: 'points' | 'money' | 'percent' | 'reopen_close' | 'reopen_bid';
    swap_long: number;
    swap_short: number;
    swap_days_in_year: number;
    swap_multipliers: Record<string, number>; 

    // Futures tab
    splice_type: 'none' | 'unadjusted' | 'adjusted';
    splice_date_extension: string;
    splice_shift_days: number;

    // Options tab
    option_type: 'call' | 'put';
    option_style: 'american' | 'european';
    strike_price: number;

    // Bonds tab
    bond_face_value: number;
    bond_accrued_interest: number;
}

export const DEFAULT_SYMBOL_DRAFT: SymbolDraft = {
    symbol: '',
    digits: 5,
    contract_size: 100000.0,
    currency: 'USD',
    margin_initial: 1.0,
    margin_maintenance: 1.0,
    spread_base: 10,
    session_hours: 'MON,00:00-24:00;TUE,00:00-24:00;WED,00:00-24:00;THU,00:00-24:00;FRI,00:00-24:00',

    description: '',
    isin: '',
    intl_name: '',
    exchange: '',
    category: '',
    cfi: '',
    sector: '',
    industry: '',
    country: '',
    basis: '',
    info_page: '',
    quote_source: '',
    bg_color: '#ffffff',
    market_depth: 0,
    fixed_spread: 0,
    spread_balance_bid: 0,
    spread_balance_ask: 0,
    chart_mode: 'bid',

    base_currency: 'EUR',
    profit_currency: 'USD',
    margin_currency: 'EUR',

    allow_realtime_quotes: true,
    allow_negative_prices: false,
    save_raw_prices: false,
    receive_market_stats: true,
    soft_filter_level: 5,
    soft_filter_repeats: 3,
    hard_filter_level: 15,
    hard_filter_repeats: 3,
    discard_filter_level: 50,
    min_spread: 0,
    max_spread: 0,
    gap_mode_level: 5,
    gap_disable_ticks: 3,
    delay_subscriptions: 0,

    calculation: 'Forex',
    trade_mode: 'full',
    gtc_mode: 0,
    limit_stop_level: 0,
    freeze_level: 0,
    max_quote_delay: 15,
    expiration_flags: ['gtc', 'day'],
    orders_allowed: ['market', 'limit', 'stop', 'sltp'],
    min_volume: 0.01,
    max_volume: 100.0,
    step_volume: 0.01,
    limit_volume: 0.0,

    execution_mode: 'Instant',
    instant_max_time_dev: 5,
    instant_fast_requotes: true,
    request_timeout: 10,
    request_confirm: false,

    exclude_long_pnl: false,
    calc_hedged_larger_leg: false,
    recalc_margin_eod: true,
    check_before_execution: true,
    check_on_sltp: true,

    rate_market_buy_init: 1.0,
    rate_market_buy_maint: 1.0,
    rate_market_sell_init: 1.0,
    rate_market_sell_maint: 1.0,
    rate_limit_buy_init: 1.0,
    rate_limit_buy_maint: 1.0,
    rate_limit_sell_init: 1.0,
    rate_limit_sell_maint: 1.0,

    enable_swaps: true,
    swap_type: 'points',
    swap_long: -0.5,
    swap_short: -0.2,
    swap_days_in_year: 360,
    swap_multipliers: {
        'Mon': 1,
        'Tue': 1,
        'Wed': 3,
        'Thu': 1,
        'Fri': 1,
        'Sat': 0,
        'Sun': 0
    },

    splice_type: 'none',
    splice_date_extension: '',
    splice_shift_days: 0,

    option_type: 'call',
    option_style: 'american',
    strike_price: 0.0,

    bond_face_value: 100.0,
    bond_accrued_interest: 0.0
};

export interface SymbolDraftContextType {
    draft: SymbolDraft;
    setDraft: React.Dispatch<React.SetStateAction<SymbolDraft>>;
    errors: Record<string, string>;
    setErrors: React.Dispatch<React.SetStateAction<Record<string, string>>>;
    isEditing: boolean;
}

export const SymbolDraftContext = React.createContext<SymbolDraftContextType | undefined>(undefined);

export function useSymbolDraft() {
    const context = React.useContext(SymbolDraftContext);
    if (!context) {
        throw new Error('useSymbolDraft must be used within SymbolDraftProvider');
    }
    return context;
}

```

---

<a id='browser-modules-symbols-modal-symbolsettingsmodal-tsx'></a>
### 63. `browser/modules/symbols/modal/SymbolSettingsModal.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { SymbolDraft, DEFAULT_SYMBOL_DRAFT, SymbolDraftContext } from './SymbolDraftContext';
import { BulkEditBanner } from './BulkEditBanner';
import { CommonTab } from './tabs/CommonTab';
import { CurrencyTab } from './tabs/CurrencyTab';
import { QuotesTab } from './tabs/QuotesTab';
import { TradeTab } from './tabs/TradeTab';
import { ExecutionTab } from './tabs/ExecutionTab';
import { MarginTab } from './tabs/MarginTab';
import { MarginRatesTab } from './tabs/MarginRatesTab';
import { SwapsTab } from './tabs/SwapsTab';
import { SessionsTab } from './tabs/SessionsTab';
import { FuturesTab } from './tabs/FuturesTab';
import { OptionsTab } from './tabs/OptionsTab';
import { BondsTab } from './tabs/BondsTab';
import { API } from '../../api';

interface SymbolSettingsModalProps {
    symbolName: string | null; // Comma-separated names if bulk editing
    initialPath?: string;
    onClose: () => void;
    onSaved: () => void;
}

export function SymbolSettingsModal({ symbolName, initialPath = '', onClose, onSaved }: SymbolSettingsModalProps): React.ReactElement {
    const [draft, setDraft] = React.useState<SymbolDraft>(DEFAULT_SYMBOL_DRAFT);
    const [activeTab, setActiveTab] = React.useState('common');
    const [errors, setErrors] = React.useState<Record<string, string>>({});
    const [loading, setLoading] = React.useState(false);
    const [saveError, setSaveError] = React.useState<string | null>(null);

    const selectedNames = symbolName ? symbolName.split(',') : [];
    const isBulk = selectedNames.length > 1;
    const isEditing = selectedNames.length > 0;

    // Load details
    React.useEffect(() => {
        if (isEditing && !isBulk) {
            setLoading(true);
            API.getSymbolDetail(selectedNames[0])
                .then(data => {
                    let parsedSettings = {};
                    if (data.settings_json) {
                        try {
                            parsedSettings = JSON.parse(data.settings_json);
                        } catch {}
                    }
                    setDraft({
                        ...DEFAULT_SYMBOL_DRAFT,
                        symbol: data.symbol,
                        digits: data.digits,
                        contract_size: data.contract_size,
                        currency: data.currency,
                        margin_initial: data.margin_initial,
                        margin_maintenance: data.margin_maintenance,
                        spread_base: data.spread_base,
                        session_hours: data.session_hours,
                        ...parsedSettings
                    } as any);
                })
                .catch(err => {
                    setSaveError(err.message || 'Failed to fetch symbol specifications.');
                })
                .finally(() => {
                    setLoading(false);
                });
        } else if (initialPath) {
            setDraft(prev => ({
                ...prev,
                symbol: initialPath
            }));
        }
    }, [symbolName, initialPath]);

    // Derive tab strips dynamically based on Trade Tab's "Calculation" field
    const visibleTabs = React.useMemo(() => {
        const base = [
            { id: 'common', label: 'Common' },
            { id: 'currency', label: 'Currency' },
            { id: 'quotes', label: 'Quotes' },
            { id: 'trade', label: 'Trade' },
            { id: 'execution', label: 'Execution' },
            { id: 'margin', label: 'Margin' },
            { id: 'marginRates', label: 'Margin Rates' },
            { id: 'swaps', label: 'Swaps' },
            { id: 'sessions', label: 'Sessions' }
        ];

        const calc = draft.calculation;
        if (calc === 'Exchange Futures' || calc === 'Exchange FORTS Futures') {
            base.push({ id: 'futures', label: 'Futures' });
        } else if (calc === 'Exchange Option') {
            base.push({ id: 'options', label: 'Options' });
        } else if (calc === 'Exchange Bonds' || calc === 'Exchange MOEXBonds') {
            base.push({ id: 'bonds', label: 'Bonds' });
        }
        return base;
    }, [draft.calculation]);

    const validateAll = (): boolean => {
        const nextErrors: Record<string, string> = {};

        if (!draft.symbol.trim()) {
            nextErrors.symbol = 'Symbol name cannot be empty.';
        }

        setErrors(nextErrors);
        return Object.keys(nextErrors).length === 0;
    };

    const handleSave = async (e: React.FormEvent) => {
        e.preventDefault();
        setSaveError(null);

        if (!validateAll()) {
            setSaveError('Please correct validation warnings before saving.');
            return;
        }

        setLoading(true);
        try {
            // Trim name
            const trimmedSymbolName = draft.symbol.trim();

            if (isBulk) {
                // If postfix copy is active (postfix starting with .)
                const isPostfixCopy = trimmedSymbolName.startsWith('.');
                
                for (const name of selectedNames) {
                    if (isPostfixCopy) {
                        // Create copy EURUSD -> EURUSD.x
                        const copyName = name + trimmedSymbolName;
                        const payload = {
                            symbol: copyName,
                            digits: draft.digits,
                            contract_size: draft.contract_size,
                            currency: draft.currency,
                            margin_initial: draft.margin_initial,
                            margin_maintenance: draft.margin_maintenance,
                            spread_base: draft.spread_base,
                            session_hours: draft.session_hours,
                            settings_json: JSON.stringify({ ...draft, symbol: copyName })
                        };
                        await API.createSymbol(payload);
                    } else {
                        // Apply partial bulk updates
                        const original = await API.getSymbolDetail(name);
                        let origSettings = {};
                        if (original.settings_json) {
                            try { origSettings = JSON.parse(original.settings_json); } catch {}
                        }

                        // Overwrite only settings draft
                        const mergedSettings = { ...origSettings, ...draft };
                        delete mergedSettings.symbol;
                        delete mergedSettings.digits;
                        delete mergedSettings.contract_size;
                        delete mergedSettings.currency;
                        delete mergedSettings.margin_initial;
                        delete mergedSettings.margin_maintenance;
                        delete mergedSettings.spread_base;
                        delete mergedSettings.session_hours;

                        const payload = {
                            symbol: name,
                            digits: draft.digits,
                            contract_size: draft.contract_size,
                            currency: draft.currency,
                            margin_initial: draft.margin_initial,
                            margin_maintenance: draft.margin_maintenance,
                            spread_base: draft.spread_base,
                            session_hours: draft.session_hours,
                            settings_json: JSON.stringify(mergedSettings)
                        };
                        await API.updateSymbol(name, payload);
                    }
                }
            } else {
                // Single symbol add or update
                const settingsData = { ...draft } as any;
                delete settingsData.symbol;
                delete settingsData.digits;
                delete settingsData.contract_size;
                delete settingsData.currency;
                delete settingsData.margin_initial;
                delete settingsData.margin_maintenance;
                delete settingsData.spread_base;
                delete settingsData.session_hours;

                const payload = {
                    symbol: trimmedSymbolName,
                    digits: draft.digits,
                    contract_size: draft.contract_size,
                    currency: draft.currency,
                    margin_initial: draft.margin_initial,
                    margin_maintenance: draft.margin_maintenance,
                    spread_base: draft.spread_base,
                    session_hours: draft.session_hours,
                    settings_json: JSON.stringify(settingsData)
                };

                if (isEditing) {
                    await API.updateSymbol(selectedNames[0], payload);
                } else {
                    await API.createSymbol(payload);
                }
            }

            onSaved();
            onClose();
        } catch (err: any) {
            setSaveError(err.message || 'Failed to save symbol specifications.');
        } finally {
            setLoading(false);
        }
    };

    const renderActiveTabContent = () => {
        switch (activeTab) {
            case 'common': return <CommonTab />;
            case 'currency': return <CurrencyTab />;
            case 'quotes': return <QuotesTab />;
            case 'trade': return <TradeTab />;
            case 'execution': return <ExecutionTab />;
            case 'margin': return <MarginTab />;
            case 'marginRates': return <MarginRatesTab />;
            case 'swaps': return <SwapsTab />;
            case 'sessions': return <SessionsTab />;
            case 'futures': return <FuturesTab />;
            case 'options': return <OptionsTab />;
            case 'bonds': return <BondsTab />;
            default: return <CommonTab />;
        }
    };

    return (
        <SymbolDraftContext.Provider value={{ draft, setDraft, errors, setErrors, isEditing }}>
            <div className="adm-modal-overlay" onClick={onClose}>
                <div className="adm-modal" style={{ width: 750, height: '65vh', display: 'flex', flexDirection: 'column', overflow: 'hidden' }} onClick={e => e.stopPropagation()}>
                    <div className="adm-modal-header">
                        <h2>
                            <i className="codicon codicon-graph" style={{ marginRight: 8, color: '#2ecc71' }} />
                            {isBulk ? 'Bulk Edit Symbol Configurations' : isEditing ? `Symbol Settings — ${selectedNames[0]}` : 'Add New Financial Symbol'}
                        </h2>
                        <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                    </div>

                    {isBulk && <BulkEditBanner count={selectedNames.length} />}

                    <div className="adm-tabs" style={{ padding: '0 16px', borderBottom: '1px solid var(--theia-border)', flexShrink: 0 }}>
                        {visibleTabs.map(t => (
                            <button 
                                key={t.id} 
                                type="button"
                                className={`adm-tab ${activeTab === t.id ? 'active' : ''} ${errors.symbol && t.id === 'common' ? 'tab-error' : ''}`}
                                onClick={() => setActiveTab(t.id)}
                            >
                                {t.label}
                                {errors.symbol && t.id === 'common' && <span className="adm-tab-error-dot" />}
                            </button>
                        ))}
                    </div>

                    <div className="adm-modal-body" style={{ flex: 1, overflow: 'hidden', padding: '12px 16px', display: 'flex', flexDirection: 'column' }}>
                        {loading && (
                            <div style={{ position: 'absolute', inset: 0, background: 'rgba(0,0,0,0.1)', display: 'flex', justifyContent: 'center', alignItems: 'center', zIndex: 10 }}>
                                <span>Ingesting details...</span>
                            </div>
                        )}
                        
                        {saveError && (
                            <div className="adm-hint" style={{ background: 'var(--theia-inputValidation-errorBackground)', color: 'var(--theia-errorForeground)', margin: '0 0 16px 0' }}>
                                <i className="codicon codicon-error" /> {saveError}
                            </div>
                        )}

                        {renderActiveTabContent()}
                    </div>

                    <div className="adm-modal-footer" style={{ borderTop: '1px solid var(--theia-border)' }}>
                        <button type="button" className="adm-btn adm-btn-primary" onClick={handleSave} disabled={loading}>
                            OK
                        </button>
                        <button type="button" className="adm-btn" onClick={onClose} disabled={loading}>
                            Cancel
                        </button>
                    </div>
                </div>
            </div>
        </SymbolDraftContext.Provider>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-bondstab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/BondsTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function BondsTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#3498db', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    B
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure bond debt instrument specifications, face par values, and accrued interest parameters.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 8 }}>
                {/* Left Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Par Value
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Face Value:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            step="0.01" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="Bond face par value" 
                            value={draft.bond_face_value} 
                            onChange={e => updateField('bond_face_value', parseFloat(e.target.value) || 0.0)} 
                        />
                    </div>
                </div>

                {/* Right Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Interest Accumulation
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Accrued Interest:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            step="0.0001" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="Accumulated interest index" 
                            value={draft.bond_accrued_interest} 
                            onChange={e => updateField('bond_accrued_interest', parseFloat(e.target.value) || 0.0)} 
                        />
                    </div>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-commontab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/CommonTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function CommonTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#f39c12', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    $
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    The setting up of main parameters of the symbol. Please specify its name, description, and other parameters.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px' }}>
                {/* Left Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Symbol:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            required 
                            value={draft.symbol}
                            onChange={e => updateField('symbol', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Exchange:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.exchange}
                            onChange={e => updateField('exchange', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>ISIN:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.isin}
                            onChange={e => updateField('isin', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>CFI:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.cfi}
                            onChange={e => updateField('cfi', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Basis:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.basis}
                            onChange={e => updateField('basis', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Source:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.quote_source}
                            onChange={e => updateField('quote_source', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Background:</span>
                        <div style={{ flex: 1, display: 'flex', gap: 6, alignItems: 'center' }}>
                            <input 
                                type="color"
                                style={{ width: 30, height: 20, border: 'none', cursor: 'pointer', padding: 0 }}
                                value={draft.bg_color}
                                onChange={e => updateField('bg_color', e.target.value)}
                            />
                            <input 
                                className="adm-input" 
                                style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                value={draft.bg_color}
                                onChange={e => updateField('bg_color', e.target.value)}
                            />
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Digits:</span>
                        <select 
                            className="adm-select" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.digits}
                            onChange={e => updateField('digits', parseInt(e.target.value) || 0)}
                        >
                            <option value={0}>0</option>
                            <option value={1}>1</option>
                            <option value={2}>2</option>
                            <option value={3}>3</option>
                            <option value={4}>4</option>
                            <option value={5}>5</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Spread:</span>
                        <div style={{ flex: 1, display: 'flex', gap: 6, alignItems: 'center' }}>
                            <input 
                                className="adm-input" 
                                style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                type="number"
                                value={draft.fixed_spread}
                                onChange={e => updateField('fixed_spread', parseInt(e.target.value) || 0)}
                            />
                            <span>pt</span>
                        </div>
                    </div>
                </div>

                {/* Right Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Description:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.description}
                            onChange={e => updateField('description', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>International:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.intl_name}
                            onChange={e => updateField('intl_name', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Sector:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.sector}
                            onChange={e => updateField('sector', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Industry:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.industry}
                            onChange={e => updateField('industry', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Country:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.country}
                            onChange={e => updateField('country', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Category:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.category}
                            onChange={e => updateField('category', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Page:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.info_page}
                            onChange={e => updateField('info_page', e.target.value)}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Market depth:</span>
                        <select 
                            className="adm-select" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.market_depth}
                            onChange={e => updateField('market_depth', parseInt(e.target.value) || 0)}
                        >
                            <option value={0}>off</option>
                            <option value={5}>5</option>
                            <option value={10}>10</option>
                            <option value={20}>20</option>
                            <option value={32}>32</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Chart mode:</span>
                        <select 
                            className="adm-select" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.chart_mode}
                            onChange={e => updateField('chart_mode', e.target.value)}
                        >
                            <option value="bid">by bid price</option>
                            <option value="last">by last price</option>
                        </select>
                    </div>
                </div>
            </div>

            {/* Slider Spread balance */}
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                <span style={{ width: 80, textAlign: 'right', opacity: 0.8 }}>Spread balance:</span>
                <div style={{ flex: 1, display: 'flex', alignItems: 'center', gap: 10 }}>
                    <input 
                        type="range"
                        min="-100"
                        max="100"
                        style={{ flex: 1, cursor: 'pointer', height: 16 }}
                        value={draft.spread_balance_bid}
                        onChange={e => {
                            const val = parseInt(e.target.value) || 0;
                            updateField('spread_balance_bid', val);
                            updateField('spread_balance_ask', -val);
                        }}
                    />
                    <span style={{ width: 100, fontSize: 11 }}>{draft.spread_balance_bid} bid / {draft.spread_balance_ask} ask</span>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-currencytab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/CurrencyTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function CurrencyTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 12, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '8px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#3498db', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    €
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Specify financial accounting currencies. Base currency represents the asset units, Profit currency calculates trade returns, and Margin currency holds collateral.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', marginTop: 8 }}>
                {/* Left Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Base currency:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            required 
                            placeholder="e.g. EUR"
                            value={draft.base_currency}
                            onChange={e => updateField('base_currency', e.target.value.toUpperCase())}
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Profit currency:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            required 
                            placeholder="e.g. USD"
                            value={draft.profit_currency}
                            onChange={e => updateField('profit_currency', e.target.value.toUpperCase())}
                        />
                    </div>
                </div>

                {/* Right Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Margin currency:</span>
                        <input 
                            className="adm-input" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            required 
                            placeholder="e.g. EUR"
                            value={draft.margin_currency}
                            onChange={e => updateField('margin_currency', e.target.value.toUpperCase())}
                        />
                    </div>
                </div>
            </div>

            <div className="adm-hint" style={{ marginTop: 'auto', marginBottom: 0, padding: '8px 12px' }}>
                <i className="codicon codicon-info" style={{ marginRight: 6 }} />
                Platform Lock: Standard fiat currencies decimal precision is fixed by system conventions. Overrides apply only to custom cryptocurrencies.
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-executiontab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/ExecutionTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function ExecutionTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#34495e', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    E
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure execution modes and order routing paths for trade request processing.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 8 }}>
                {/* Left Column (Routing Mode Selection) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Execution mode:</span>
                        <select 
                            className="adm-select" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.execution_mode} 
                            onChange={e => updateField('execution_mode', e.target.value)}
                        >
                            <option value="Instant">Instant Execution</option>
                            <option value="Request">Request Execution</option>
                            <option value="Market">Market Execution</option>
                            <option value="Exchange">Exchange Execution</option>
                        </select>
                    </div>

                    {draft.execution_mode === 'Instant' && (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max dev (pts):</span>
                                <input 
                                    className="adm-input" 
                                    type="number" 
                                    style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                    value={draft.instant_max_time_dev} 
                                    onChange={e => updateField('instant_max_time_dev', parseInt(e.target.value) || 0)} 
                                />
                            </div>

                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', paddingLeft: 10 }}>
                                <input 
                                    type="checkbox" 
                                    checked={draft.instant_fast_requotes} 
                                    onChange={e => updateField('instant_fast_requotes', e.target.checked)} 
                                />
                                Auto-confirm requotes within dev
                            </label>
                        </>
                    )}

                    {draft.execution_mode === 'Request' && (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Timeout (sec):</span>
                                <input 
                                    className="adm-input" 
                                    type="number" 
                                    style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                                    value={draft.request_timeout} 
                                    onChange={e => updateField('request_timeout', parseInt(e.target.value) || 10)} 
                                />
                            </div>

                            <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', paddingLeft: 10 }}>
                                <input 
                                    type="checkbox" 
                                    checked={draft.request_confirm} 
                                    onChange={e => updateField('request_confirm', e.target.checked)} 
                                />
                                Require manager check first
                            </label>
                        </>
                    )}
                </div>

                {/* Right Column (Info Display Cards) */}
                <div style={{ display: 'flex', flexDirection: 'column' }}>
                    {draft.execution_mode === 'Market' && (
                        <div className="adm-hint" style={{ margin: 0, padding: '8px 12px' }}>
                            <i className="codicon codicon-info" style={{ marginRight: 6 }} />
                            <strong>Market Mode:</strong> Trades execute at the next available server price. Requotes are disabled because prices are accepted upfront.
                        </div>
                    )}

                    {draft.execution_mode === 'Exchange' && (
                        <div className="adm-hint" style={{ margin: 0, padding: '8px 12px', borderLeft: '3px solid #e67e22' }}>
                            <i className="codicon codicon-info" style={{ marginRight: 6, color: '#e67e22' }} />
                            <strong>Exchange Mode:</strong> Routed directly to liquidity providers. Limit and freeze boundaries are bypassed, leaving filling choices to the exchange order book.
                        </div>
                    )}

                    {draft.execution_mode === 'Instant' && (
                        <div className="adm-hint" style={{ margin: 0, padding: '8px 12px' }}>
                            <i className="codicon codicon-info" style={{ marginRight: 6 }} />
                            <strong>Instant Mode:</strong> Order executes exactly at the requested price. If the price moves beyond client-side deviation, the broker returns a requote.
                        </div>
                    )}

                    {draft.execution_mode === 'Request' && (
                        <div className="adm-hint" style={{ margin: 0, padding: '8px 12px' }}>
                            <i className="codicon codicon-info" style={{ marginRight: 6 }} />
                            <strong>Request Mode:</strong> Client asks for quotes first, then sends confirmation to execute. Best suited for manual voice or high-ticket desk dealers.
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-futurestab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/FuturesTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function FuturesTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#1abc9c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    F
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure exchange futures contract specifications, settlement price, and expiry rollover splice settings.
                    These parameters are normally fed automatically by the gateway.
                </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 8 }}>
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Contract Bounds
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 120, textAlign: 'right', opacity: 0.8 }}>Settlement price:</span>
                        <input className="adm-input" type="number" step="0.0001" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.strike_price} onChange={e => updateField('strike_price', parseFloat(e.target.value) || 0.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 120, textAlign: 'right', opacity: 0.8 }}>Min price bound:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.bond_face_value} onChange={e => updateField('bond_face_value', parseFloat(e.target.value) || 0.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 120, textAlign: 'right', opacity: 0.8 }}>Max price bound:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.bond_accrued_interest} onChange={e => updateField('bond_accrued_interest', parseFloat(e.target.value) || 0.0)} />
                    </div>
                </div>

                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Splice Rollover
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Splice type:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.splice_type} onChange={e => updateField('splice_type', e.target.value)}>
                            <option value="none">None</option>
                            <option value="unadjusted">Unadjusted</option>
                            <option value="adjusted">Adjusted</option>
                        </select>
                    </div>

                    {draft.splice_type !== 'none' && (
                        <>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Expiry date:</span>
                                <input className="adm-input" type="date" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.splice_date_extension} onChange={e => updateField('splice_date_extension', e.target.value)} />
                            </div>

                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Shift days:</span>
                                <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.splice_shift_days} onChange={e => updateField('splice_shift_days', parseInt(e.target.value) || 0)} />
                            </div>
                        </>
                    )}
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-marginratestab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/MarginRatesTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function MarginRatesTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#9b59b6', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    %
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Specify margin requirements multiplier rates per transaction order type and stock collateral valuations.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Market & Limits) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', gap: 8, fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        <span style={{ width: 90 }}>Order Type</span>
                        <span style={{ flex: 1, textAlign: 'center' }}>Initial</span>
                        <span style={{ flex: 1, textAlign: 'center' }}>Maint</span>
                    </div>

                    <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <span style={{ width: 90, opacity: 0.8 }}>Market Buy:</span>
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_market_buy_init} onChange={e => updateField('rate_market_buy_init', parseFloat(e.target.value) || 1.0)} />
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_market_buy_maint} onChange={e => updateField('rate_market_buy_maint', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <span style={{ width: 90, opacity: 0.8 }}>Market Sell:</span>
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_market_sell_init} onChange={e => updateField('rate_market_sell_init', parseFloat(e.target.value) || 1.0)} />
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_market_sell_maint} onChange={e => updateField('rate_market_sell_maint', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <span style={{ width: 90, opacity: 0.8 }}>Buy Limit:</span>
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_buy_init} onChange={e => updateField('rate_limit_buy_init', parseFloat(e.target.value) || 1.0)} />
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_buy_maint} onChange={e => updateField('rate_limit_buy_maint', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <span style={{ width: 90, opacity: 0.8 }}>Sell Limit:</span>
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_sell_init} onChange={e => updateField('rate_limit_sell_init', parseFloat(e.target.value) || 1.0)} />
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_sell_maint} onChange={e => updateField('rate_limit_sell_maint', parseFloat(e.target.value) || 1.0)} />
                    </div>
                </div>

                {/* Right Column (Stops & Collaterals) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', gap: 8, fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        <span style={{ width: 90 }}>Order Type</span>
                        <span style={{ flex: 1, textAlign: 'center' }}>Initial</span>
                        <span style={{ flex: 1, textAlign: 'center' }}>Maint</span>
                    </div>

                    <div style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                        <span style={{ width: 90, opacity: 0.8 }}>Stops (Buy/Sell):</span>
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_buy_init} onChange={e => updateField('rate_limit_buy_init', parseFloat(e.target.value) || 1.0)} />
                        <input className="adm-input" type="number" step="0.1" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.rate_limit_buy_maint} onChange={e => updateField('rate_limit_buy_maint', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginTop: 4, marginBottom: 2 }}>
                        Collateral Values
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Liquidity Margin:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} placeholder="0.00" value={draft.discard_filter_level} onChange={e => updateField('discard_filter_level', parseFloat(e.target.value) || 0.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Currency Margin:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.delay_subscriptions} onChange={e => updateField('delay_subscriptions', parseFloat(e.target.value) || 0.0)} />
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-margintab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/MarginTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function MarginTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#9b59b6', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    M
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure margin calculations, absolute multiplier overrides, and automated transaction validation limits.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 8 }}>
                
                {/* Left Column (Rates overrides) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Multiplier Overrides
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 120, textAlign: 'right', opacity: 0.8 }}>Initial Margin rate:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            step="0.01" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.margin_initial} 
                            onChange={e => updateField('margin_initial', parseFloat(e.target.value) || 0.0)} 
                        />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 120, textAlign: 'right', opacity: 0.8 }}>Maintenance rate:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            step="0.01" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            value={draft.margin_maintenance} 
                            onChange={e => updateField('margin_maintenance', parseFloat(e.target.value) || 0.0)} 
                        />
                    </div>

                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginTop: 4, marginBottom: 2 }}>
                        Hedging Margin Calculation
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.calc_hedged_larger_leg} 
                            onChange={e => updateField('calc_hedged_larger_leg', e.target.checked)} 
                        />
                        Calculate using larger leg size
                    </label>
                </div>

                {/* Right Column (Verification Triggers) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Verification Checks
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.check_before_execution} 
                            onChange={e => updateField('check_before_execution', e.target.checked)} 
                        />
                        Check before execution
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.check_on_sltp} 
                            onChange={e => updateField('check_on_sltp', e.target.checked)} 
                        />
                        Check on SL / TP order triggers
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.exclude_long_pnl} 
                            onChange={e => updateField('exclude_long_pnl', e.target.checked)} 
                        />
                        Exclude long PnL from free margin
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.recalc_margin_eod} 
                            onChange={e => updateField('recalc_margin_eod', e.target.checked)} 
                        />
                        Recalculate rate EOD
                    </label>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-optionstab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/OptionsTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function OptionsTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e67e22', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    O
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure options derivative settings. Options can be Call or Put, and structured as American or European exercise styles.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1, marginTop: 8 }}>
                {/* Left Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Option Classification
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Option Type:</span>
                        <div style={{ flex: 1, display: 'flex', gap: 12 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer' }}>
                                <input type="radio" name="opt-type" checked={draft.option_type === 'call'} onChange={() => updateField('option_type', 'call')} />
                                Call
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer' }}>
                                <input type="radio" name="opt-type" checked={draft.option_type === 'put'} onChange={() => updateField('option_type', 'put')} />
                                Put
                            </label>
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Option Style:</span>
                        <div style={{ flex: 1, display: 'flex', gap: 12 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer' }}>
                                <input type="radio" name="opt-style" checked={draft.option_style === 'american'} onChange={() => updateField('option_style', 'american')} />
                                American
                            </label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 4, cursor: 'pointer' }}>
                                <input type="radio" name="opt-style" checked={draft.option_style === 'european'} onChange={() => updateField('option_style', 'european')} />
                                European
                            </label>
                        </div>
                    </div>
                </div>

                {/* Right Column */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 8 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Pricing Limits
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 90, textAlign: 'right', opacity: 0.8 }}>Strike Price:</span>
                        <input 
                            className="adm-input" 
                            type="number" 
                            step="0.0001" 
                            style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }}
                            placeholder="Strike boundary price" 
                            value={draft.strike_price} 
                            onChange={e => updateField('strike_price', parseFloat(e.target.value) || 0.0)} 
                        />
                    </div>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-quotestab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/QuotesTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

export function QuotesTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const isExchangeOrDOM = draft.market_depth > 0 || draft.calculation.toLowerCase().includes('exchange');
    const isFutures = draft.calculation.toLowerCase().includes('futures');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#2ecc71', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    Q
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure pricing data feeds transmission, subscription delays, and automated quote filtration thresholds.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1 }}>
                
                {/* Left Column (Transmission & Gaps) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Ingestion Transmission
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 20 }}>
                        <input type="checkbox" checked={draft.allow_realtime_quotes} onChange={e => updateField('allow_realtime_quotes', e.target.checked)} />
                        Allow real-time quotes feeds
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 20 }}>
                        <input type="checkbox" checked={draft.save_raw_prices} onChange={e => updateField('save_raw_prices', e.target.checked)} />
                        Save raw, unfiltered ticks
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 20 }}>
                        <input type="checkbox" checked={draft.receive_market_stats} onChange={e => updateField('receive_market_stats', e.target.checked)} />
                        Receive market statistics
                    </label>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, cursor: 'pointer', height: 20, opacity: isFutures ? 1 : 0.6 }}>
                        <input type="checkbox" disabled={!isFutures} checked={isFutures && draft.allow_negative_prices} onChange={e => updateField('allow_negative_prices', e.target.checked)} />
                        Allow negative prices (Futures)
                    </label>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginTop: 4 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Delay (mins):</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.delay_subscriptions} onChange={e => updateField('delay_subscriptions', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginTop: 4, marginBottom: 2 }}>
                        Gap Pricing Checks
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Gap Level (pts):</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.gap_mode_level} onChange={e => updateField('gap_mode_level', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Disable ticks:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.gap_disable_ticks} onChange={e => updateField('gap_disable_ticks', parseInt(e.target.value) || 0)} />
                    </div>
                </div>

                {/* Right Column (Filtration limits) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, opacity: isExchangeOrDOM ? 0.6 : 1 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Spam Filtration {isExchangeOrDOM && '(N/A for DOM)'}
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Soft level (pts):</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.soft_filter_level} onChange={e => updateField('soft_filter_level', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Soft repeats:</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.soft_filter_repeats} onChange={e => updateField('soft_filter_repeats', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Hard level (pts):</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.hard_filter_level} onChange={e => updateField('hard_filter_level', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Hard repeats:</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.hard_filter_repeats} onChange={e => updateField('hard_filter_repeats', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Discard level (pts):</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.discard_filter_level} onChange={e => updateField('discard_filter_level', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Min spread limit:</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.min_spread} onChange={e => updateField('min_spread', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 110, textAlign: 'right', opacity: 0.8 }}>Max spread limit:</span>
                        <input disabled={isExchangeOrDOM} className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.max_spread} onChange={e => updateField('max_spread', parseInt(e.target.value) || 0)} />
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-sessionstab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/SessionsTab.tsx`

```tsx
// @ts-nocheck
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';
import { DayScheduleEditor } from './sessions/DayScheduleEditor';

const DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];

export function SessionsTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();
    const [selectedDay, setSelectedDay] = React.useState<string | null>(null);

    const [schedules, setSchedules] = React.useState<Record<string, {
        quotes: Array<{ start: string, end: string }>;
        trade: Array<{ start: string, end: string }>;
        separateTrade: boolean;
    }>>({});

    React.useEffect(() => {
        const initialScheds: typeof schedules = {};
        DAYS.forEach(day => {
            initialScheds[day] = {
                quotes: [{ start: '00:00', end: '24:00' }],
                trade: [{ start: '00:00', end: '24:00' }],
                separateTrade: false
            };
        });
        setSchedules(initialScheds);
    }, []);

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const handleSaveDaySchedule = (day: string, daySched: any) => {
        setSchedules(prev => ({ ...prev, [day]: daySched }));
        setSelectedDay(null);
    };

    const [useLimits, setUseLimits] = React.useState(false);
    const [limitFrom, setLimitFrom] = React.useState('');
    const [limitTo, setLimitTo] = React.useState('');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#f1c40f', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    T
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure active timetables for quotes collection, client trade sessions, and calendar contract expirations.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1.1fr 0.9fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Timetable) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Weekly Timetable
                    </div>

                    <div className="adm-table-wrap" style={{ border: '1px solid var(--theia-border)', height: 140, overflowY: 'auto' }}>
                        <table className="adm-table" style={{ fontSize: 10 }}>
                            <thead>
                                <tr>
                                    <th>Day</th>
                                    <th>Quotes Session</th>
                                    <th>Trade Session</th>
                                </tr>
                            </thead>
                            <tbody>
                                {DAYS.map(day => {
                                    const sched = schedules[day] || { quotes: [], trade: [], separateTrade: false };
                                    const quotesStr = sched.quotes.map(q => `${q.start}-${q.end}`).join(', ') || 'No session';
                                    const tradeStr = sched.separateTrade 
                                        ? (sched.trade.map(t => `${t.start}-${t.end}`).join(', ') || 'No session')
                                        : 'Same as Quotes';

                                    return (
                                        <tr 
                                            key={day} 
                                            className={selectedDay === day ? 'selected' : ''}
                                            onClick={() => setSelectedDay(day)}
                                            onDoubleClick={() => setSelectedDay(day)}
                                            style={{ cursor: 'pointer', height: 18 }}
                                        >
                                            <td><strong>{day.substring(0, 3)}</strong></td>
                                            <td>{quotesStr}</td>
                                            <td>{tradeStr}</td>
                                        </tr>
                                    );
                                })}
                            </tbody>
                        </table>
                    </div>
                </div>

                {/* Right Column (Expiration limits) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 10, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Contract Expirations
                    </div>

                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input type="checkbox" checked={useLimits} onChange={e => setUseLimits(e.target.checked)} />
                        Limit active date interval
                    </label>

                    {useLimits && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 50, opacity: 0.8 }}>From:</span>
                                <input className="adm-input" type="date" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={limitFrom} onChange={e => setLimitFrom(e.target.value)} />
                            </div>
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 50, opacity: 0.8 }}>To:</span>
                                <input className="adm-input" type="date" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={limitTo} onChange={e => setLimitTo(e.target.value)} />
                            </div>
                        </div>
                    )}
                </div>
            </div>

            {selectedDay && (
                <DayScheduleEditor 
                    day={selectedDay}
                    schedule={schedules[selectedDay]}
                    onClose={() => setSelectedDay(null)}
                    onSave={(sched) => handleSaveDaySchedule(selectedDay, sched)}
                />
            )}
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-swapstab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/SwapsTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

const SWAP_TYPES = [
    { value: 'points', label: 'In points of spread' },
    { value: 'money', label: 'In absolute money values' },
    { value: 'percent', label: 'In percentage terms of position value' },
    { value: 'reopen_close', label: 'Reopen by Close Price' },
    { value: 'reopen_bid', label: 'Reopen by Bid Price' }
];

const DAYS_IN_YEAR = [360, 365, 366];

export function SwapsTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const handleMultiplierChange = (day: string, value: number) => {
        const nextMult = { ...draft.swap_multipliers, [day]: value };
        updateField('swap_multipliers', nextMult);
    };

    const applyForexPreset = () => {
        setDraft(prev => ({
            ...prev,
            swap_multipliers: {
                'Mon': 1, 'Tue': 1, 'Wed': 3, 'Thu': 1, 'Fri': 1, 'Sat': 0, 'Sun': 0
            }
        }));
    };

    const applyAllWeekPreset = () => {
        setDraft(prev => ({
            ...prev,
            swap_multipliers: {
                'Mon': 1, 'Tue': 1, 'Wed': 1, 'Thu': 1, 'Fri': 1, 'Sat': 1, 'Sun': 1
            }
        }));
    };

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e67e22', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    S
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Configure automatic rollover swap interest charges, day multipliers, and holiday accrual rules.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1.1fr 0.9fr', gap: '8px 24px', flex: 1, marginTop: 4 }}>
                
                {/* Left Column (Rates overrides) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <label style={{ display: 'flex', alignItems: 'center', gap: 6, fontSize: 11, cursor: 'pointer', height: 20 }}>
                        <input 
                            type="checkbox" 
                            checked={draft.enable_swaps} 
                            onChange={e => updateField('enable_swaps', e.target.checked)} 
                        />
                        <strong>Enable rollover swaps calculation</strong>
                    </label>

                    <fieldset disabled={!draft.enable_swaps} style={{ border: 'none', margin: 0, padding: 0, display: 'flex', flexDirection: 'column', gap: 6 }}>
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Swap Type:</span>
                            <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.swap_type} onChange={e => updateField('swap_type', e.target.value)}>
                                {SWAP_TYPES.map(t => <option key={t.value} value={t.value}>{t.label}</option>)}
                            </select>
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Long rate:</span>
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.swap_long} onChange={e => updateField('swap_long', parseFloat(e.target.value) || 0.0)} />
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Short rate:</span>
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.swap_short} onChange={e => updateField('swap_short', parseFloat(e.target.value) || 0.0)} />
                        </div>

                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Yearly base:</span>
                            <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.swap_days_in_year} onChange={e => updateField('swap_days_in_year', parseInt(e.target.value) || 360)}>
                                {DAYS_IN_YEAR.map(d => <option key={d} value={d}>{d} Days</option>)}
                            </select>
                        </div>

                        {draft.swap_type === 'money' && (
                            <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Currency Basis:</span>
                                <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.currency} onChange={e => updateField('currency', e.target.value)}>
                                    <option value="base">Base currency</option>
                                    <option value="margin">Margin currency</option>
                                    <option value="profit">Profit currency</option>
                                </select>
                            </div>
                        )}
                    </fieldset>
                </div>

                {/* Right Column (Multiplier grid) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6, opacity: draft.enable_swaps ? 1 : 0.6 }}>
                    <div style={{ fontWeight: 'bold', fontSize: 11, borderBottom: '1px solid var(--theia-border)', paddingBottom: 2, marginBottom: 2 }}>
                        Accrual Multipliers
                    </div>

                    <div style={{ display: 'flex', gap: 4, marginBottom: 6 }}>
                        <button type="button" className="adm-btn" style={{ flex: 1, fontSize: 10, padding: '2px 4px' }} disabled={!draft.enable_swaps} onClick={applyForexPreset}>Wed x3</button>
                        <button type="button" className="adm-btn" style={{ flex: 1, fontSize: 10, padding: '2px 4px' }} disabled={!draft.enable_swaps} onClick={applyAllWeekPreset}>All x1</button>
                    </div>

                    <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
                        {Object.keys(draft.swap_multipliers).map(day => (
                            <div key={day} style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                                <span style={{ width: 40, opacity: 0.8, textTransform: 'capitalize' }}>{day}:</span>
                                <input 
                                    disabled={!draft.enable_swaps}
                                    className="adm-input" 
                                    type="number"
                                    style={{ flex: 1, height: 18, padding: '2px 4px', fontSize: 11, textAlign: 'center' }}
                                    value={draft.swap_multipliers[day]} 
                                    onChange={e => handleMultiplierChange(day, parseInt(e.target.value) || 0)} 
                                />
                            </div>
                        ))}
                    </div>
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-tradetab-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/TradeTab.tsx`

```tsx
import * as React from 'react';
import { useSymbolDraft } from '../SymbolDraftContext';

const CALC_MODES = [
    'Forex',
    'Forex No Leverage',
    'CFD',
    'CFD Index',
    'CFD Leverage',
    'Exchange Stocks',
    'Exchange MOEX Stocks',
    'Exchange Bonds',
    'Exchange MOEXBonds',
    'Exchange Futures',
    'Exchange FORTS Futures',
    'Exchange Option',
    'Collateral'
];

const TRADE_MODES = [
    { value: 'disabled', label: 'Disabled (No trading)' },
    { value: 'long_only', label: 'Long Only (Buys allowed)' },
    { value: 'short_only', label: 'Short Only (Sells allowed)' },
    { value: 'close_only', label: 'Close Only (Liquidation only)' },
    { value: 'full', label: 'Full Access (Long & Short)' }
];

export function TradeTab(): React.ReactElement {
    const { draft, setDraft } = useSymbolDraft();

    const updateField = (field: keyof typeof draft, val: any) => {
        setDraft(prev => ({ ...prev, [field]: val }));
    };

    const handleCheckboxArrayChange = (field: 'expiration_flags' | 'orders_allowed', value: string, checked: boolean) => {
        const current = draft[field] || [];
        const next = checked ? [...current, value] : current.filter(item => item !== value);
        updateField(field, next);
    };

    const isForex = draft.calculation.startsWith('Forex');

    return (
        <div style={{ display: 'flex', flexDirection: 'column', height: '100%', gap: 10, fontSize: 11 }}>
            {/* Top header info banner side-by-side */}
            <div style={{ display: 'flex', gap: 12, alignItems: 'center', background: 'var(--theia-sideBarSectionHeader-background)', padding: '6px 12px', borderRadius: 4 }}>
                <div style={{ width: 32, height: 32, display: 'flex', justifyContent: 'center', alignItems: 'center', background: '#e74c3c', borderRadius: 4, color: '#fff', fontSize: 18, fontWeight: 'bold' }}>
                    T
                </div>
                <div style={{ flex: 1, opacity: 0.9, lineHeight: 1.3 }}>
                    Set up contract size, calculation models, trade session modes, and volume order parameters.
                </div>
            </div>

            {/* Grid fields */}
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '8px 24px', flex: 1 }}>
                
                {/* Left Column (Contract Details) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Contract size:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.contract_size} onChange={e => updateField('contract_size', parseFloat(e.target.value) || 0.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Tick size:</span>
                        <input className="adm-input" type="number" step="0.00001" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.margin_initial} onChange={e => updateField('margin_initial', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Tick value:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.margin_maintenance} onChange={e => updateField('margin_maintenance', parseFloat(e.target.value) || 1.0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Calculation:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.calculation} onChange={e => updateField('calculation', e.target.value)}>
                            {CALC_MODES.map(c => <option key={c} value={c}>{c}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Trade mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.trade_mode} onChange={e => updateField('trade_mode', e.target.value)}>
                            {TRADE_MODES.map(m => <option key={m.value} value={m.value}>{m.label}</option>)}
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Limit/Stop level:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.limit_stop_level} onChange={e => updateField('limit_stop_level', parseInt(e.target.value) || 0)} />
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Freeze level:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.freeze_level} onChange={e => updateField('freeze_level', parseInt(e.target.value) || 0)} />
                    </div>
                </div>

                {/* Right Column (Permissions & Volume bounds) */}
                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>GTC mode:</span>
                        <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.gtc_mode} onChange={e => updateField('gtc_mode', parseInt(e.target.value) || 0)}>
                            <option value={0}>Day canceled</option>
                            <option value={1}>Kept GTC</option>
                            <option value={2}>Kept except SL/TP</option>
                        </select>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Max quote delay:</span>
                        <input className="adm-input" type="number" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.max_quote_delay} onChange={e => updateField('max_quote_delay', parseInt(e.target.value) || 15)} />
                    </div>

                    <div style={{ display: 'flex', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Filling flags:</span>
                        <div style={{ display: 'flex', gap: 8, fontSize: 10 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.orders_allowed.includes('fok')} onChange={e => handleCheckboxArrayChange('orders_allowed', 'fok', e.target.checked)} /> FOK</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.orders_allowed.includes('ioc')} onChange={e => handleCheckboxArrayChange('orders_allowed', 'ioc', e.target.checked)} /> IOC</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.orders_allowed.includes('boc')} onChange={e => handleCheckboxArrayChange('orders_allowed', 'boc', e.target.checked)} /> BOC</label>
                        </div>
                    </div>

                    <div style={{ display: 'flex', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Expirations:</span>
                        <div style={{ display: 'flex', gap: 8, fontSize: 10 }}>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('gtc')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'gtc', e.target.checked)} /> GTC</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('day')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'day', e.target.checked)} /> Day</label>
                            <label style={{ display: 'flex', alignItems: 'center', gap: 2 }}><input type="checkbox" checked={draft.expiration_flags.includes('time')} onChange={e => handleCheckboxArrayChange('expiration_flags', 'time', e.target.checked)} /> Time</label>
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Volumes (min/max):</span>
                        <div style={{ flex: 1, display: 'flex', gap: 4 }}>
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.min_volume} onChange={e => updateField('min_volume', parseFloat(e.target.value) || 0.01)} />
                            <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 4px', fontSize: 11 }} value={draft.max_volume} onChange={e => updateField('max_volume', parseFloat(e.target.value) || 100.0)} />
                        </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                        <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Volume step:</span>
                        <input className="adm-input" type="number" step="0.01" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.step_volume} onChange={e => updateField('step_volume', parseFloat(e.target.value) || 0.01)} />
                    </div>

                    {isForex && (
                        <div style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
                            <span style={{ width: 100, textAlign: 'right', opacity: 0.8 }}>Profit conversion:</span>
                            <select className="adm-select" style={{ flex: 1, height: 20, padding: '2px 6px', fontSize: 11 }} value={draft.limit_volume} onChange={e => updateField('limit_volume', parseInt(e.target.value) || 0)}>
                                <option value={0}>By deals records</option>
                                <option value={1}>By real-time rates</option>
                            </select>
                        </div>
                    )}
                </div>

            </div>
        </div>
    );
}

```

---

<a id='browser-modules-symbols-modal-tabs-sessions-dayscheduleeditor-tsx'></a>
### 63. `browser/modules/symbols/modal/tabs/sessions/DayScheduleEditor.tsx`

```tsx
import * as React from 'react';

interface SessionBlock {
    start: string;
    end: string;
}

interface DayScheduleEditorProps {
    day: string;
    schedule: {
        quotes: SessionBlock[];
        trade: SessionBlock[];
        separateTrade: boolean;
    };
    onClose: () => void;
    onSave: (schedule: any) => void;
}

export function DayScheduleEditor({ day, schedule, onClose, onSave }: DayScheduleEditorProps): React.ReactElement {
    const [quotes, setQuotes] = React.useState<SessionBlock[]>([...schedule.quotes]);
    const [trade, setTrade] = React.useState<SessionBlock[]>([...schedule.trade]);
    const [separateTrade, setSeparateTrade] = React.useState(schedule.separateTrade);

    const handleAddBlock = (type: 'quotes' | 'trade') => {
        const newBlock = { start: '08:00', end: '17:00' };
        if (type === 'quotes') {
            setQuotes([...quotes, newBlock]);
        } else {
            setTrade([...trade, newBlock]);
        }
    };

    const handleRemoveBlock = (type: 'quotes' | 'trade', index: number) => {
        if (type === 'quotes') {
            setQuotes(quotes.filter((_, i) => i !== index));
        } else {
            setTrade(trade.filter((_, i) => i !== index));
        }
    };

    const handleTimeChange = (type: 'quotes' | 'trade', index: number, field: 'start' | 'end', value: string) => {
        if (type === 'quotes') {
            const next = [...quotes];
            next[index] = { ...next[index], [field]: value };
            setQuotes(next);
        } else {
            const next = [...trade];
            next[index] = { ...next[index], [field]: value };
            setTrade(next);
        }
    };

    const handleSave = () => {
        onSave({
            quotes,
            trade: separateTrade ? trade : [...quotes],
            separateTrade
        });
    };

    return (
        <div className="adm-modal-overlay" style={{ zIndex: 1200 }} onClick={onClose}>
            <div className="adm-modal" style={{ width: 440 }} onClick={e => e.stopPropagation()}>
                <div className="adm-modal-header">
                    <h2>Edit Time Sessions — {day}</h2>
                    <button type="button" className="adm-modal-close" onClick={onClose}>×</button>
                </div>
                <div className="adm-modal-body" style={{ display: 'flex', flexDirection: 'column', gap: 14 }}>
                    
                    {/* Quotes Session Blocks */}
                    <div>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                            <span style={{ fontSize: 12, fontWeight: 'bold' }}>Quotes Sessions</span>
                            <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('quotes')}>
                                <i className="codicon codicon-add" /> Add Session
                            </button>
                        </div>

                        {quotes.length === 0 ? (
                            <div style={{ padding: 12, background: 'var(--theia-sideBarSectionHeader-background)', fontSize: 11, textAlign: 'center', opacity: 0.6 }}>
                                No quotes session active. Market will be offline.
                            </div>
                        ) : (
                            <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                                {quotes.map((block, idx) => (
                                    <div key={idx} style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                                        <input className="adm-input" type="time" style={{ width: 110, fontSize: 11, padding: 3, height: 22 }} value={block.start} onChange={e => handleTimeChange('quotes', idx, 'start', e.target.value)} />
                                        <span>to</span>
                                        <input className="adm-input" type="time" style={{ width: 110, fontSize: 11, padding: 3, height: 22 }} value={block.end} onChange={e => handleTimeChange('quotes', idx, 'end', e.target.value)} />
                                        <button type="button" className="adm-icon-btn" onClick={() => handleRemoveBlock('quotes', idx)}>
                                            <i className="codicon codicon-trash" style={{ color: 'var(--theia-errorForeground)' }} />
                                        </button>
                                    </div>
                                ))}
                            </div>
                        )}
                    </div>

                    {/* Trade Session Separate Checkbox */}
                    <div className="adm-form-row" style={{ flexDirection: 'row', alignItems: 'center', gap: 8, borderTop: '1px solid var(--theia-border)', paddingTop: 10 }}>
                        <input type="checkbox" id="sep-trade" checked={separateTrade} onChange={e => setSeparateTrade(e.target.checked)} />
                        <label htmlFor="sep-trade" style={{ cursor: 'pointer', margin: 0, fontSize: 12 }}>Enable separate trading sessions (different from quotes)</label>
                    </div>

                    {/* Trade Session Blocks */}
                    {separateTrade && (
                        <div>
                            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 }}>
                                <span style={{ fontSize: 12, fontWeight: 'bold' }}>Trade Sessions</span>
                                <button type="button" className="adm-btn" style={{ fontSize: 10, padding: '2px 8px' }} onClick={() => handleAddBlock('trade')}>
                                    <i className="codicon codicon-add" /> Add Session
                                </button>
                            </div>

                            {trade.length === 0 ? (
                                <div style={{ padding: 12, background: 'var(--theia-sideBarSectionHeader-background)', fontSize: 11, textAlign: 'center', opacity: 0.6 }}>
                                    No trading session active. Clients cannot execute trades.
                                </div>
                            ) : (
                                <div style={{ display: 'flex', flexDirection: 'column', gap: 6 }}>
                                    {trade.map((block, idx) => (
                                        <div key={idx} style={{ display: 'flex', gap: 8, alignItems: 'center' }}>
                                            <input className="adm-input" type="time" style={{ width: 110, fontSize: 11, padding: 3, height: 22 }} value={block.start} onChange={e => handleTimeChange('trade', idx, 'start', e.target.value)} />
                                            <span>to</span>
                                            <input className="adm-input" type="time" style={{ width: 110, fontSize: 11, padding: 3, height: 22 }} value={block.end} onChange={e => handleTimeChange('trade', idx, 'end', e.target.value)} />
                                            <button type="button" className="adm-icon-btn" onClick={() => handleRemoveBlock('trade', idx)}>
                                                <i className="codicon codicon-trash" style={{ color: 'var(--theia-errorForeground)' }} />
                                            </button>
                                        </div>
                                    ))}
                                </div>
                            )}
                        </div>
                    )}
                </div>
                <div className="adm-modal-footer">
                    <button type="button" className="adm-btn adm-btn-primary" onClick={handleSave}>Save changes</button>
                    <button type="button" className="adm-btn" onClick={onClose}>Cancel</button>
                </div>
            </div>
        </div>
    );
}

```

---

<a id='browser-style-index-css'></a>
### 63. `browser/style/index.css`

```css
/* ================================================================
   MT5 Admin Tree Widget — Theia sidebar panel styles
   ================================================================ */

/* ── Container ─────────────────────────────────────────────────── */
.mt5-admin-tree-widget {
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow: hidden;
    background: var(--theia-sideBar-background);
    color: var(--theia-sideBar-foreground);
    font-size: 12px;
    font-family: var(--theia-ui-font-family);
}

.mt5-admin-tree-container {
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow: hidden;
}

/* ── Header ────────────────────────────────────────────────────── */
.mt5-admin-tree-header {
    display: flex;
    align-items: center;
    padding: 4px 12px;
    height: 22px;
    background: var(--theia-sideBarSectionHeader-background);
    border-bottom: 1px solid var(--theia-sideBarSectionHeader-border, var(--theia-contrastBorder));
    flex-shrink: 0;
}

.mt5-admin-tree-header-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: var(--theia-sideBarSectionHeader-foreground, var(--theia-foreground));
    opacity: 0.9;
}

/* ── Scrollable body ───────────────────────────────────────────── */
.mt5-admin-tree-body {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    padding: 4px 0;
}

.mt5-admin-tree-body::-webkit-scrollbar {
    width: 6px;
}
.mt5-admin-tree-body::-webkit-scrollbar-thumb {
    background: var(--theia-scrollbarSlider-background);
    border-radius: 3px;
}

/* ── Tree rows ─────────────────────────────────────────────────── */
.mt5-admin-tree-row {
    display: flex;
    align-items: center;
    height: 22px;
    cursor: pointer;
    border-radius: 3px;
    margin: 0 4px;
    white-space: nowrap;
    overflow: hidden;
    user-select: none;
    transition: background 0.1s ease;
    gap: 4px;
}

.mt5-admin-tree-row:hover {
    background: var(--theia-list-hoverBackground);
}

.mt5-admin-tree-row.selected {
    background: var(--theia-list-activeSelectionBackground);
    color: var(--theia-list-activeSelectionForeground);
}

/* ── Arrow ─────────────────────────────────────────────────────── */
.mt5-admin-tree-arrow {
    display: inline-flex;
    align-items: center;
    width: 16px;
    flex-shrink: 0;
    opacity: 0;
    font-size: 12px;
    color: var(--theia-foreground);
}

.mt5-admin-tree-arrow.visible {
    opacity: 0.7;
}

.mt5-admin-tree-row:hover .mt5-admin-tree-arrow.visible,
.mt5-admin-tree-row.selected .mt5-admin-tree-arrow.visible {
    opacity: 1;
}

/* ── Node icon ─────────────────────────────────────────────────── */
.mt5-admin-tree-icon {
    font-size: 14px;
    flex-shrink: 0;
    opacity: 0.8;
    color: var(--theia-symbolIcon-variableForeground, var(--theia-foreground));
}

.mt5-admin-tree-row.selected .mt5-admin-tree-icon {
    opacity: 1;
    color: var(--theia-list-activeSelectionForeground);
}

/* ── Label ─────────────────────────────────────────────────────── */
.mt5-admin-tree-label {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 12.5px;
    line-height: 22px;
}

/* ── Children wrapper ──────────────────────────────────────────── */
.mt5-admin-tree-children {
    /* children inherit full row margins from their own .mt5-admin-tree-row */
}

/* ================================================================
   MT5 Admin Content Widget — main area tab panel
   ================================================================ */

.mt5-admin-content-widget {
    display: flex;
    flex-direction: column;
    height: 100%;
    background: var(--theia-editor-background);
    color: var(--theia-foreground);
    font-family: var(--theia-ui-font-family);
    overflow: auto;
}

.mt5-admin-content-panel {
    display: flex;
    flex-direction: column;
    min-height: 100%;
}

/* ── Content header ────────────────────────────────────────────── */
.mt5-admin-content-header {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 20px 28px 16px;
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    background: var(--theia-editorGroupHeader-tabsBackground);
}

.mt5-admin-content-header-icon {
    font-size: 24px;
    opacity: 0.85;
    color: var(--theia-symbolIcon-variableForeground, #4fc3f7);
}

.mt5-admin-content-title {
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: 0.2px;
    color: var(--theia-foreground);
    border: none;
}

/* ── Content body ──────────────────────────────────────────────── */
.mt5-admin-content-body {
    flex: 1;
    padding: 24px 28px;
}

/* ── Placeholder ───────────────────────────────────────────────── */
.mt5-admin-section-placeholder {
    max-width: 720px;
}

.mt5-admin-section-desc {
    font-size: 13.5px;
    line-height: 1.7;
    color: var(--theia-descriptionForeground);
    margin-bottom: 24px;
}

.mt5-admin-section-wip {
    display: inline-flex;
    align-items: center;
    padding: 10px 16px;
    background: var(--theia-inputValidation-infoBackground);
    border: 1px solid var(--theia-inputValidation-infoBorder);
    border-radius: 4px;
    font-size: 12px;
    color: var(--theia-inputValidation-infoForeground);
    gap: 6px;
}

.mt5-admin-section-wip code {
    font-family: var(--theia-code-font-family, monospace);
    font-size: 11px;
    background: var(--theia-textBlockQuote-background);
    padding: 1px 5px;
    border-radius: 3px;
}

/* ================================================================
   Shared Admin Page Styles (adm-*)
   Used by: NetworkClusterPage, GroupsPage, ClientsPage, etc.
   ================================================================ */

/* ── Page wrapper ───────────────────────────────────────────────── */
.adm-page {
    display: flex;
    flex-direction: column;
    height: 100%;
    overflow: hidden;
    font-size: 12px;
    font-family: var(--theia-ui-font-family);
    color: var(--theia-foreground);
}

/* ── Toolbar ────────────────────────────────────────────────────── */
.adm-toolbar {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 6px 12px;
    background: var(--theia-editorGroupHeader-tabsBackground);
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    flex-shrink: 0;
    flex-wrap: wrap;
}

.adm-toolbar-sep {
    width: 1px;
    height: 18px;
    background: var(--theia-widget-border, var(--theia-contrastBorder));
    margin: 0 4px;
}

/* ── Buttons ────────────────────────────────────────────────────── */
.adm-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    padding: 3px 10px;
    font-size: 11.5px;
    border: 1px solid var(--theia-button-border, var(--theia-contrastBorder));
    background: var(--theia-button-secondaryBackground);
    color: var(--theia-button-secondaryForeground);
    border-radius: 3px;
    cursor: pointer;
    white-space: nowrap;
    transition: background 0.12s;
}
.adm-btn:hover:not(:disabled) { background: var(--theia-button-secondaryHoverBackground); }
.adm-btn:disabled { opacity: 0.4; cursor: not-allowed; }

.adm-btn-primary {
    background: var(--theia-button-background);
    color: var(--theia-button-foreground);
    border-color: transparent;
}
.adm-btn-primary:hover:not(:disabled) { background: var(--theia-button-hoverBackground); }

.adm-btn-danger {
    background: transparent;
    color: var(--theia-errorForeground);
    border-color: var(--theia-errorForeground);
    opacity: 0.85;
}
.adm-btn-danger:hover:not(:disabled) { background: var(--theia-inputValidation-errorBackground); opacity: 1; }

.adm-icon-btn {
    background: none; border: none; cursor: pointer;
    color: var(--theia-foreground); opacity: 0.6;
    display: flex; align-items: center; padding: 2px 4px; border-radius: 3px;
}
.adm-icon-btn:hover { opacity: 1; background: var(--theia-list-hoverBackground); }

/* ── Tabs ───────────────────────────────────────────────────────── */
.adm-tabs {
    display: flex;
    gap: 0;
    padding: 0 12px;
    background: var(--theia-editorGroupHeader-tabsBackground);
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    flex-shrink: 0;
}
.adm-tab {
    padding: 6px 16px;
    font-size: 12px;
    border: none; background: none;
    cursor: pointer;
    color: var(--theia-descriptionForeground);
    border-bottom: 2px solid transparent;
    transition: all 0.12s;
}
.adm-tab:hover { color: var(--theia-foreground); }
.adm-tab.active {
    color: var(--theia-tab-activeForeground, var(--theia-foreground));
    border-bottom-color: var(--theia-focusBorder);
}

/* ── Hint bar ───────────────────────────────────────────────────── */
.adm-hint {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 5px 14px;
    font-size: 11px;
    color: var(--theia-descriptionForeground);
    background: var(--theia-inputValidation-infoBackground);
    border-bottom: 1px solid var(--theia-inputValidation-infoBorder);
    flex-shrink: 0;
}

/* ── Table ──────────────────────────────────────────────────────── */
.adm-table-wrap {
    flex: 1;
    overflow: auto;
}
.adm-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 11.5px;
}
.adm-table thead {
    position: sticky;
    top: 0;
    background: var(--theia-editorGroupHeader-tabsBackground);
    z-index: 1;
}
.adm-table th {
    padding: 5px 10px;
    text-align: left;
    font-weight: 600;
    font-size: 11px;
    letter-spacing: 0.3px;
    color: var(--theia-descriptionForeground);
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    white-space: nowrap;
}
.adm-table td {
    padding: 4px 10px;
    border-bottom: 1px solid var(--theia-widget-border, transparent);
    vertical-align: middle;
    white-space: nowrap;
}
.adm-table tbody tr:hover { background: var(--theia-list-hoverBackground); }
.adm-table tbody tr.selected { background: var(--theia-list-activeSelectionBackground); color: var(--theia-list-activeSelectionForeground); }
.adm-table tbody tr.adm-row-disabled { opacity: 0.45; }

/* ── Numbers ────────────────────────────────────────────────────── */
.adm-num { text-align: right; font-variant-numeric: tabular-nums; font-family: monospace; }
.adm-pos { color: var(--theia-gitDecoration-addedResourceForeground, #27ae60) !important; }
.adm-neg { color: var(--theia-errorForeground) !important; }

/* ── Badges / Tags ──────────────────────────────────────────────── */
.adm-badge, .adm-tag {
    display: inline-flex;
    align-items: center;
    padding: 1px 7px;
    border-radius: 10px;
    font-size: 10.5px;
    font-weight: 600;
    background: var(--theia-badge-background);
    color: var(--theia-badge-foreground);
    border: 1px solid transparent;
}
.adm-side-badge {
    display: inline-flex; align-items: center;
    padding: 1px 8px; border-radius: 3px;
    font-size: 10.5px; font-weight: 700;
    letter-spacing: 0.3px;
}
.adm-side-badge.buy  { background: #27ae6022; color: #27ae60; border: 1px solid #27ae6066; }
.adm-side-badge.sell { background: #e74c3c22; color: #e74c3c; border: 1px solid #e74c3c66; }

.adm-chip {
    display: inline-flex; align-items: center;
    padding: 1px 8px; margin: 2px 2px;
    background: var(--theia-badge-background);
    color: var(--theia-badge-foreground);
    border-radius: 10px; font-size: 10.5px;
}
.adm-dot {
    display: inline-block; width: 8px; height: 8px;
    border-radius: 50%; margin-right: 6px;
}

/* ── Status dot ─────────────────────────────────────────────────── */
.adm-status-dot {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
}
.adm-status-dot.online  { background: var(--theia-successForeground, #27ae60); box-shadow: 0 0 4px #27ae6088; }
.adm-status-dot.offline { background: var(--theia-errorForeground, #e74c3c); }

/* ── CPU bar ────────────────────────────────────────────────────── */
.adm-cpu-bar {
    display: flex; align-items: center; gap: 6px;
    min-width: 80px;
}
.adm-cpu-fill {
    height: 4px; border-radius: 2px; transition: width 0.3s;
    background: var(--theia-successForeground);
}

/* ── Search ─────────────────────────────────────────────────────── */
.adm-search-wrap {
    display: flex; align-items: center; gap: 6px;
    background: var(--theia-input-background);
    border: 1px solid var(--theia-input-border);
    border-radius: 3px;
    padding: 2px 8px;
}
.adm-search {
    background: none; border: none; outline: none;
    color: var(--theia-input-foreground);
    font-size: 11.5px;
    width: 180px;
}

/* ── Inputs & Selects ───────────────────────────────────────────── */
.adm-input {
    background: var(--theia-input-background);
    border: 1px solid var(--theia-input-border);
    color: var(--theia-input-foreground);
    border-radius: 3px; padding: 3px 7px; font-size: 12px;
    outline: none;
}
.adm-input:focus { border-color: var(--theia-focusBorder); }
.adm-select {
    background: var(--theia-dropdown-background);
    border: 1px solid var(--theia-dropdown-border);
    color: var(--theia-dropdown-foreground);
    border-radius: 3px; padding: 3px 7px; font-size: 12px;
    cursor: pointer; outline: none;
}

/* ── Toggle ─────────────────────────────────────────────────────── */
.adm-toggle {
    padding: 2px 6px; border-radius: 3px; font-size: 10px;
    border: 1px solid; cursor: pointer; background: none;
}
.adm-toggle.on  { color: var(--theia-successForeground); border-color: var(--theia-successForeground); }
.adm-toggle.off { color: var(--theia-errorForeground);   border-color: var(--theia-errorForeground); }

/* ── Split view ─────────────────────────────────────────────────── */
.adm-split-view {
    display: flex; flex: 1; overflow: hidden; gap: 0;
}

/* ── Detail panel ───────────────────────────────────────────────── */
.adm-detail-panel {
    display: flex; flex-direction: column;
    flex: 1; border-left: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    background: var(--theia-sideBar-background);
    overflow: hidden; min-width: 220px;
}
.adm-detail-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 8px 12px;
    font-size: 12px; font-weight: 600;
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    background: var(--theia-sideBarSectionHeader-background);
    flex-shrink: 0;
}
.adm-detail-body {
    flex: 1; overflow-y: auto; padding: 8px 0;
}
.adm-detail-section {
    font-size: 10px; font-weight: 700; letter-spacing: 0.8px;
    text-transform: uppercase; color: var(--theia-descriptionForeground);
    padding: 10px 12px 4px;
}
.adm-kv {
    display: flex; justify-content: space-between; align-items: center;
    padding: 3px 12px; font-size: 11.5px;
    border-bottom: 1px solid var(--theia-widget-border, transparent);
    gap: 8px;
}
.adm-kv > span:first-child { color: var(--theia-descriptionForeground); flex-shrink: 0; }
.adm-kv > *:last-child { text-align: right; }
.adm-detail-footer {
    display: flex; gap: 6px; padding: 10px 12px;
    border-top: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    flex-shrink: 0;
}

/* ── Routing condition chips ────────────────────────────────────── */
.adm-condition-chip {
    display: inline-flex; align-items: center;
    background: var(--theia-badge-background);
    color: var(--theia-badge-foreground);
    padding: 1px 6px; border-radius: 10px;
    font-size: 10px; margin-right: 4px;
}
.adm-condition-row {
    display: flex; align-items: center; gap: 6px;
    padding: 3px 12px; font-size: 11.5px;
}
.adm-condition-type  { color: var(--theia-descriptionForeground); }
.adm-condition-op    { opacity: 0.6; }

/* ── Modal ──────────────────────────────────────────────────────── */
.adm-modal-overlay {
    position: fixed; inset: 0; z-index: 9999;
    background: rgba(0,0,0,0.55);
    display: flex; align-items: center; justify-content: center;
}
.adm-modal {
    background: var(--theia-editor-background);
    border: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    border-radius: 6px; width: 460px; max-width: 90vw;
    display: flex; flex-direction: column;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.adm-modal-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 12px 16px;
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
}
.adm-modal-header h2 { margin: 0; font-size: 14px; }
.adm-modal-close {
    background: none; border: none; cursor: pointer;
    color: var(--theia-foreground); opacity: 0.6; font-size: 16px;
}
.adm-modal-close:hover { opacity: 1; }
.adm-modal-body { padding: 16px; display: flex; flex-direction: column; gap: 12px; }
.adm-modal-footer {
    display: flex; gap: 8px; justify-content: flex-end;
    padding: 12px 16px;
    border-top: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
}
.adm-form-row {
    display: flex; flex-direction: column; gap: 4px;
}
.adm-form-row label { font-size: 11.5px; font-weight: 600; color: var(--theia-descriptionForeground); }
.adm-hint-text { font-size: 10.5px; color: var(--theia-descriptionForeground); opacity: 0.7; }

/* ── Status bar ─────────────────────────────────────────────────── */
.adm-statusbar {
    display: flex; align-items: center; gap: 6px;
    padding: 3px 12px; font-size: 11px;
    background: var(--theia-statusBar-background);
    color: var(--theia-statusBar-foreground);
    border-top: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    flex-shrink: 0;
}
.adm-sep { opacity: 0.4; }

/* ── Code ───────────────────────────────────────────────────────── */
.adm-code {
    font-family: var(--theia-code-font-family, monospace);
    font-size: 10.5px;
    background: var(--theia-textBlockQuote-background);
    padding: 1px 4px; border-radius: 2px;
}

/* ── Form body (settings panels) ────────────────────────────────── */
.adm-form-body {
    flex: 1;
    overflow-y: auto;
    padding: 12px 20px;
}
.adm-form-section {
    font-size: 10.5px;
    font-weight: 700;
    letter-spacing: 0.8px;
    text-transform: uppercase;
    color: var(--theia-descriptionForeground);
    padding: 14px 0 6px;
    border-bottom: 1px solid var(--theia-widget-border, var(--theia-contrastBorder));
    margin-bottom: 8px;
}
.adm-form-row {
    display: flex;
    flex-direction: column;
    gap: 3px;
    margin-bottom: 10px;
}
.adm-form-row label {
    font-size: 11.5px;
    font-weight: 600;
    color: var(--theia-descriptionForeground);
    display: flex;
    align-items: center;
    gap: 6px;
}
.adm-form-row .adm-input,
.adm-form-row .adm-select,
.adm-form-row textarea.adm-input {
    width: 320px;
    max-width: 100%;
}
textarea.adm-input {
    resize: vertical;
    font-family: var(--theia-ui-font-family);
    min-height: 40px;
}

/* ================================================================
   MT5 Admin Groups Module Layout additions
   ================================================================ */

/* ── Split navigation tree pane ────────────────────────────────── */
.adm-tree-pane {
    background: var(--theia-sideBar-background);
    flex-shrink: 0;
    user-select: none;
    box-sizing: border-box;
}

.adm-tree-pane-row {
    display: flex;
    align-items: center;
    height: 22px;
    padding: 0 8px;
    cursor: pointer;
    border-radius: 3px;
    margin: 2px 0;
    font-size: 12px;
    color: var(--theia-foreground);
    transition: background 0.1s ease;
    gap: 4px;
}

.adm-tree-pane-row:hover {
    background: var(--theia-list-hoverBackground);
}

.adm-tree-pane-row.active {
    background: var(--theia-list-activeSelectionBackground);
    color: var(--theia-list-activeSelectionForeground);
}

/* ── Context Menu ──────────────────────────────────────────────── */
.adm-context-menu {
    position: fixed;
    z-index: 1200;
    background: var(--theia-menu-background);
    border: 1px solid var(--theia-menu-border, var(--theia-widget-border));
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
    padding: 4px 0;
    border-radius: 4px;
    min-width: 160px;
    font-family: var(--theia-ui-font-family);
    user-select: none;
}

.adm-context-item {
    display: flex;
    align-items: center;
    width: 100%;
    border: none;
    background: transparent;
    color: var(--theia-menu-foreground);
    padding: 6px 12px;
    font-size: 11.5px;
    text-align: left;
    cursor: pointer;
    gap: 8px;
}

.adm-context-item:hover {
    background: var(--theia-menu-selectionBackground);
    color: var(--theia-menu-selectionForeground);
}

.adm-context-item:disabled {
    opacity: 0.4;
    cursor: not-allowed;
}

.adm-context-item-danger {
    color: var(--theia-errorForeground);
}

.adm-context-sep {
    height: 1px;
    background: var(--theia-widget-border, var(--theia-contrastBorder));
    margin: 4px 0;
}

/* ── Modal tab badges & validations ────────────────────────────── */
.adm-tab-error-dot {
    position: absolute;
    top: 4px;
    right: 4px;
    width: 6px;
    height: 6px;
    background: var(--theia-errorForeground);
    border-radius: 50%;
}

.adm-tab.tab-error {
    border-bottom: 2px solid var(--theia-errorForeground) !important;
}

/* ── Specific row states ───────────────────────────────────────── */
.adm-row-disabled {
    opacity: 0.5;
    text-decoration: line-through;
}

.adm-row-warning {
    background: rgba(240, 173, 78, 0.08) !important;
}

.adm-row-warning:hover {
    background: rgba(240, 173, 78, 0.15) !important;
}

.adm-input-error-text {
    font-size: 10.5px;
    color: var(--theia-errorForeground);
    margin-top: 3px;
    font-weight: 500;
}

.adm-form-row .adm-input.error,
.adm-form-row .adm-select.error {
    border-color: var(--theia-errorForeground) !important;
    background: var(--theia-inputValidation-errorBackground) !important;
}




```

---

<a id='common-mt5-admin-tree-ts'></a>
### 63. `common/mt5-admin-tree.ts`

```typescript
// @ts-nocheck

/**
 * MT5 Admin tree node types — mirrors the full MT5 Administrator sidebar.
 */

export interface AdminTreeNode {
    id: string;
    label: string;
    icon?: string;            // codicon name
    children?: AdminTreeNode[];
}

/**
 * Full MT5 Administrator sidebar tree, taken from the official documentation.
 * Each leaf node opens a dedicated tab in the main area.
 */
export const MT5_ADMIN_TREE: AdminTreeNode[] = [
    {
        id: 'start-page',
        label: 'Start Page',
        icon: 'home'
    },
    {
        id: 'network-cluster',
        label: 'Network Cluster',
        icon: 'server',
        children: [
            { id: 'network-cluster.servers',       label: 'Servers',         icon: 'server-environment' },
            { id: 'network-cluster.data-centers',  label: 'Data Centers',    icon: 'database' },
            { id: 'network-cluster.backup',        label: 'Backup Server',   icon: 'save' }
        ]
    },
    {
        id: 'integrations',
        label: 'Integrations',
        icon: 'plug',
        children: [
            { id: 'integrations.mail',      label: 'Mail Servers',  icon: 'mail' },
            { id: 'integrations.messenger', label: 'Messengers',    icon: 'comment-discussion' },
            { id: 'integrations.finteza',   label: 'Finteza',       icon: 'graph' }
        ]
    },
    {
        id: 'automations',
        label: 'Automations',
        icon: 'zap',
        children: [
            { id: 'automations.scenarios', label: 'Scenarios', icon: 'play' }
        ]
    },
    {
        id: 'security',
        label: 'Security',
        icon: 'shield',
        children: [
            { id: 'security.certificates',     label: 'Certificates',       icon: 'verified-filled' },
            { id: 'security.firewall',          label: 'Firewall',           icon: 'shield' },
            { id: 'security.antiddos',          label: 'Anti DDoS',          icon: 'shield-x' }
        ]
    },
    {
        id: 'time',
        label: 'Time',
        icon: 'clock'
    },
    {
        id: 'holidays',
        label: 'Holidays',
        icon: 'calendar'
    },
    {
        id: 'leverage',
        label: 'Leverage',
        icon: 'arrow-both'
    },
    {
        id: 'groups',
        label: 'Groups',
        icon: 'organization'
    },
    {
        id: 'clients-and-accounts',
        label: 'Clients & Accounts',
        icon: 'person',
        children: [
            { id: 'clients-and-accounts.allocations',      label: 'Allocations',      icon: 'list-selection' },
            { id: 'clients-and-accounts.clients',          label: 'Clients',          icon: 'organization' },
            { id: 'clients-and-accounts.managers',         label: 'Managers',         icon: 'account' },
            { id: 'clients-and-accounts.trading-accounts',  label: 'Trading Accounts',  icon: 'credit-card' }
        ]
    },
    {
        id: 'positions',
        label: 'Positions',
        icon: 'graph-scatter',
        children: [
            { id: 'positions.open',        label: 'Open Positions',          icon: 'graph-scatter' },
            { id: 'positions.summary',     label: 'Summary (Positions)',     icon: 'list-flat' },
            { id: 'positions.exposure',    label: 'Exposure (Assets)',       icon: 'pie-chart' },
            { id: 'positions.margin-call', label: 'Margin Call / Stop Out',  icon: 'warning' },
            { id: 'positions.history',     label: 'Position History',        icon: 'history' }
        ]
    },
    {
        id: 'orders',
        label: 'Orders',
        icon: 'list-ordered',
        children: [
            { id: 'orders.active',   label: 'Active Orders',   icon: 'clock' },
            { id: 'orders.history',  label: 'Order History',   icon: 'history' },
            { id: 'orders.create',   label: 'New Order',       icon: 'add' }
        ]
    },
    {
        id: 'deals',
        label: 'Deals',
        icon: 'pulse',
        children: [
            { id: 'deals.list',    label: 'Deal Log',     icon: 'list-unordered' },
            { id: 'deals.search',  label: 'Search',       icon: 'search' }
        ]
    },
    {
        id: 'payments',
        label: 'Payments',
        icon: 'credit-card',
        children: [
            { id: 'payments.list',       label: 'Payment Log',  icon: 'list-unordered' },
            { id: 'payments.systems',    label: 'Systems',      icon: 'plug' }
        ]
    },
    {
        id: 'gateways',
        label: 'Gateways',
        icon: 'radio-tower',
        children: [
            { id: 'gateways.list',    label: 'Gateway List', icon: 'list-unordered' },
            { id: 'gateways.routing', label: 'Routing',      icon: 'git-merge' }
        ]
    },
    {
        id: 'data-feeds',
        label: 'Data Feeds',
        icon: 'broadcast',
        children: [
            { id: 'data-feeds.sources',  label: 'Feed Sources', icon: 'database' },
            { id: 'data-feeds.news',     label: 'News',         icon: 'rss' }
        ]
    },
    {
        id: 'market-watch',
        label: 'Market Watch',
        icon: 'eye'
    },
    {
        id: 'plugins',
        label: 'Plugins',
        icon: 'extensions',
        children: [
            { id: 'plugins.installed', label: 'Installed',  icon: 'check' },
            { id: 'plugins.store',     label: 'App Store',  icon: 'package' }
        ]
    },
    {
        id: 'reports',
        label: 'Reports',
        icon: 'graph',
        children: [
            { id: 'reports.standard', label: 'Standard',  icon: 'list-flat' },
            { id: 'reports.custom',   label: 'Custom',    icon: 'edit' }
        ]
    },
    {
        id: 'ecn',
        label: 'ECN',
        icon: 'git-network'
    },
    {
        id: 'routing',
        label: 'Routing',
        icon: 'git-merge',
        children: [
            { id: 'routing.rules',      label: 'Routing Rules',     icon: 'list-ordered' },
            { id: 'routing.a-book',     label: 'A-Book',            icon: 'arrow-right' },
            { id: 'routing.b-book',     label: 'B-Book',            icon: 'arrow-left' },
            { id: 'routing.gateways',   label: 'LP Gateways',       icon: 'radio-tower' }
        ]
    },
    {
        id: 'funds-etf',
        label: 'Funds & ETF',
        icon: 'pie-chart',
        children: [
            { id: 'funds-etf.funds',    label: 'Funds',     icon: 'pie-chart' },
            { id: 'funds-etf.etf',      label: 'ETF',       icon: 'graph-line' }
        ]
    },
    {
        id: 'symbols',
        label: 'Symbols',
        icon: 'symbol-namespace'
    },
    {
        id: 'spreads',
        label: 'Spreads',
        icon: 'arrow-both'
    },
    {
        id: 'history-charts',
        label: '1-Min History Charts',
        icon: 'graph-line'
    },
    {
        id: 'tick-data',
        label: 'Bid/Ask/Last Ticks',
        icon: 'pulse'
    },
    {
        id: 'synchronization',
        label: 'Synchronization',
        icon: 'sync'
    },
    {
        id: 'subscriptions',
        label: 'Subscriptions',
        icon: 'rss'
    },
    {
        id: 'mailbox',
        label: 'Mailbox',
        icon: 'mail'
    },
    {
        id: 'live-update',
        label: 'Live Update',
        icon: 'cloud-download'
    },
    {
        id: 'support-center',
        label: 'Support Center',
        icon: 'question'
    },
    {
        id: 'app-store',
        label: 'App Store',
        icon: 'package'
    }
];

```

---
