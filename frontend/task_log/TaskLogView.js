import React from "react";
import { useParams } from "react-router-dom";
import { Box, Flex, VStack, Center, Grid } from "@chakra-ui/react";

import TaskLogLeftPane from "task_log/TaskLogLeftPane";
import { TaskProvider } from "tasks/contexts";
import { TaskLogProvider } from "task_log/contexts";
import TaskLogMessageStream from "task_log/TaskLogMessageStream";
import TaskResponseForm from "task_log/TaskResponseForm";

export const TaskLogView = () => {
  const { id } = useParams();

  return (
    <TaskProvider taskId={id}>
      <Flex h="100vh">
        <VStack bg="blackAlpha.800" w="20%" p={4} minH="100vh">
          <TaskLogLeftPane />
        </VStack>
        <Flex direction="column" flex="1" h="100%">
          <Box flexGrow="1" overflowY="auto">
            <Grid h="100%" templateRows="1fr auto" alignItems="end" gap={4}>
              <VStack spacing={4} ml={4} mr={4}>
                {/* Scrollable content */}
                <TaskLogMessageStream />
              </VStack>
            </Grid>
          </Box>
          <Center w="100%" p={4} boxShadow="0px -1px 4px rgba(0, 0, 0, 0.1)">
            {/* Bottom aligned section */}
            <TaskResponseForm />
          </Center>
        </Flex>
      </Flex>
    </TaskProvider>
  );
};

export default TaskLogView;
