import { Title, Card, Text, Image } from '@mantine/core';

export default function View({ viewData }) {
  const title = viewData?.title;
  const clusters = viewData?.components;

  function renderTitle() {
    return <Title order={1}>{title}</Title>;
  }

  function renderComponent(component, key) {
    if (component.type === 'box') {
      return (
        <Card key={key}>
          <Title order={3}>{component.title}</Title>
          {component.description.map((line, i) => (<Text key={i}>{line}</Text>))}
        </Card>
      );
    }
    if (component.type === 'photo') {
      return (
        <Image key={key} src={`${component.location}`} alt={component.location} w={500}/>
      );
    }
  }

  function renderCluster(cluster, index) {
    return (
      <div key={index}>
        {cluster.components.map((component, i) => renderComponent(component, i))}
      </div>
    );
  }

  return (
    <div>
      {renderTitle()}
      {clusters?.map((cluster, i) => renderCluster(cluster, i))}
    </div>
  );
}
