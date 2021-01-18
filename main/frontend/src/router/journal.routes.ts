import JournalsPage from '@/pages/journals/JournalsPage.vue';
import AddJournalPage from '@/pages/journals/AddJournalPage.vue';

const journalRoutes = [
  {
    path: '/journals',
    component: JournalsPage,
    name: 'journals',
    children: [
      {
        path: 'add',
        component: AddJournalPage,
        name: 'add-journal',
      },
    ],
  },
];

export default journalRoutes;
