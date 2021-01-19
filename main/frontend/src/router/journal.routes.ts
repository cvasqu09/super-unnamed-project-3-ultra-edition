import JournalsPage from '@/pages/journals/JournalsPage.vue';
import AddJournalPage from '@/pages/journals/AddJournalPage.vue';
import JournalsListPage from '@/pages/journals/JournalsListPage.vue';

const journalRoutes = [
  {
    path: '/journals',
    component: JournalsPage,
    children: [
      {
        path: 'add',
        component: AddJournalPage,
        name: 'add-journal',
      },
      {
        path: '/',
        component: JournalsListPage,
        name: 'journal-list',
      },
      {
        path: '*',
        redirectTo: '/',
      },
    ],
  },
];

export default journalRoutes;
